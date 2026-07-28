import bcrypt
from src.database.config import supabase
import uuid
from datetime import datetime

# Teacher Database Functions

def check_teacher_exists(username):
    response = (
        supabase
        .table("teachers")
        .select("username")
        .eq("username", username)
        .execute()
    )
    return len(response.data) > 0


def hash_pass(password):
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()


def check_pass(password, hashed_password):
    try:
        return bcrypt.checkpw(
            password.encode(),
            hashed_password.encode()
        )
    except ValueError:
        print("Invalid hash stored in database:", hashed_password)
        return False


def create_teacher(username, password, name):
    data = {
        "username": username,
        "password": hash_pass(password),
        "name": name
    }
    response = (
        supabase
        .table("teachers")
        .insert(data)
        .execute()
    )
    return response.data


def teacher_login(username, password):
    response = (
        supabase
        .table("teachers")
        .select("*")
        .eq("username", username)
        .execute()
    )

    if not response.data:
        return None
    
    teacher = response.data[0]

    print("Teacher found:", teacher)
    print("Stored hash:", teacher["password"])

    if check_pass(password, teacher["password"]):
        return teacher
    return None


# =========================
# Student Database Functions
# =========================

def get_all_students():
    response = (
        supabase
        .table("students")
        .select("*")
        .execute()
    )

    return response.data

def create_student(new_name, face_embedding=None, voice_embedding=None):
    data = {
        'name': new_name,
        'face_embedding': face_embedding,
        'voice_embedding': voice_embedding
    }

    response = supabase.table('students').insert(data).execute()
    return response.data  

def create_subject(subject_code,name,section,teacher_id):
    data = {
        "subject_code":subject_code,
        "name":name,
        "section":section,
        "teacher_id": teacher_id
    }

    response = supabase.table('subjects').insert(data).execute()
    return response.data

def get_teacher_subjects(teacher_id):
    response = supabase.table('subjects').select("*, subjects_students(count), attendance_logs(timestamp)").eq("teacher_id", teacher_id).execute()
    subjects = response.data


    for sub in subjects:
        sub['total_students'] = sub.get("subjects_students", [{}])[0].get('count', 0) if sub.get('subjects_students') else 0
        attendance = sub.get('attendance_logs', [])
        unique_sessions = len(set(log['timestamp'] for log in attendance))
        sub['total_classes'] = unique_sessions


        sub.pop('subject_student', None)
        sub.pop('attendance_logs', None)

    return subjects


def  enroll_student_to_subject(student_id, subject_id):
    data = {'student_id': student_id, "subject_id": subject_id}
    response= supabase.table('subjects_students').insert(data).execute()
    return response.data


def  unenroll_student_to_subject(student_id, subject_id):
    response= supabase.table('subjects_students').delete().eq('student_id', student_id).eq('subject_id', subject_id).execute()
    return response.data



def get_student_subjects(student_id):
    response = supabase.table('subjects_students').select('*, subjects(*)').eq('student_id', student_id).execute()
    return response.data


def get_student_attendance(student_id):
    response = supabase.table('attendance_logs').select('*, subjects(*)').eq('student_id', student_id).execute()
    return response.data


def create_attendance(logs):
    response = supabase.table('attendance_logs').insert(logs).execute()
    return response.data

def get_attendance_for_teacher(teacher_id):
    response = supabase.table('attendance_logs').select("*, subjects!inner(*)").eq('subjects.teacher_id', teacher_id).execute()
    return response.data

def delete_subject(subject_id):
    try:

        # delete related student mappings first
        supabase.table("subjects_students") \
            .delete() \
            .eq("subject_id", subject_id) \
            .execute()

        # delete attendance records
        supabase.table("attendance_logs") \
            .delete() \
            .eq("subject_id", subject_id) \
            .execute()

        # delete subject
        supabase.table("subjects") \
            .delete() \
            .eq("subject_id", subject_id) \
            .execute()

        return True

    except Exception as e:
        print(e)
        return False


def create_assignment(
    teacher_id,
    subject_id,
    assignment_title,
    max_marks,
    assignment_image,
    submission_date,
):
    # Generate a unique filename
    file_name = f"{uuid.uuid4()}_{assignment_image.name}"
    file_path = f"assignments/{subject_id}/{file_name}"

    supabase.storage.from_("assignment_images").upload(
        file_path,
        assignment_image.getvalue(),
        {
            "content-type": assignment_image.type
        }
    )

    # Insert assignment record
    data = {
    "teacher_id": teacher_id,
    "subject_id": subject_id,
    "assignment_image": file_path, 
    "max_marks": max_marks,
    "created_at": datetime.now().isoformat(),
    "submission_date":submission_date.isoformat(),
    "assignment_title":assignment_title,
}

    supabase.table("assignments").insert(data).execute()



def get_student_assignments(student_id):

    # Get subjects in which the student is enrolled
    subjects = (
        supabase.table("subjects_students")
        .select("subject_id")
        .eq("student_id", student_id)
        .execute()
    )

    if not subjects.data:
        return []

    subject_ids = [s["subject_id"] for s in subjects.data]

    # Get assignments for those subjects
    assignments = (
        supabase.table("assignments")
        .select("""
            assignment_id,
            max_marks,
            created_at,
            assignment_image,
            submission_date,
            subjects(name,
            subject_code),
            assignment_title
        """)
        .in_("subject_id", subject_ids)
        .order("created_at", desc=True)
        .execute()
    )

    result = []

    for row in assignments.data:
        result.append({
            "assignment_id": row["assignment_id"],
            "subject_name": row["subjects"]["name"],
            "subject_code": row["subjects"]["subject_code"],
            "max_marks": row["max_marks"],
            "assignment_image": row["assignment_image"],
            "created_at": row["created_at"],
            "submission_date": row["submission_date"],
            "assignment_title": row["assignment_title"],
        })

    return result



def submit_assignment(assignment_id, student_id, pdf_file,assignment_title):

    file_name = f"{uuid.uuid4()}_{pdf_file.name}"
    file_path = f"submissions/{assignment_id}/{student_id}/{file_name}"

    # Upload PDF
    supabase.storage.from_("submission_pdfs").upload(
        file_path,
        pdf_file.getvalue(),
        {
            "content-type": "application/pdf"
        }
    )

    # Get public URL
    public_url = (
        supabase.storage
        .from_("submission_pdfs")
        .get_public_url(file_path)
    )

    # Save submission
    supabase.table("assignment_submissions").insert({
        "assignment_id": assignment_id,
        "student_id": student_id,
        "assignment_title":assignment_title,
        "submission_pdf_url": public_url,
        "submitted_at": datetime.now().isoformat()
    }).execute()


def has_submitted_assignment(assignment_id, student_id):

    response = (
        supabase.table("assignment_submissions")
        .select("submission_id")
        .eq("assignment_id", assignment_id)
        .eq("student_id", student_id)
        .limit(1)
        .execute()
    )

    return len(response.data) > 0

def get_assignment_submissions(teacher_id):

    response = (
        supabase.table("assignment_submissions")
        .select("""
            submission_id,
            submitted_at,
            obtained_marks,
            assignment_id,
            submission_pdf_url,
            students(name),
            assignments(
                subject_id,
                subjects(subject_code)
            )
        """)
        .execute()
    )

    return response.data

def update_assignment_marks(submission_id, marks, remark):

    supabase.table("assignment_submissions").update({
        "obtained_marks": marks,
        "remark": remark
    }).eq(
        "submission_id",
        submission_id
    ).execute()

def get_submission_details(assignment_id, student_id):

    response = (
        supabase.table("assignment_submissions")
        .select("""
            submitted_at,
            obtained_marks,
            assignment_title,
            remark
        """)
        .eq("assignment_id", assignment_id)
        .eq("student_id", student_id)
        .single()
        .execute()
    )

    return response.data
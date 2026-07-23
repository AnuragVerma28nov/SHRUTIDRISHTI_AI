import streamlit as st
import numpy as np
import PIL as pl
import time
from datetime import datetime
from PIL import Image
from src.ui.base_layout import style_toolbar, style_background_dashboard
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.components.subject_card import subject_card
from src.database.db import has_submitted_assignment,get_student_assignments, check_teacher_exists,teacher_login,create_teacher,get_all_students,create_student, get_student_subjects,get_student_attendance, unenroll_student_to_subject
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embeddings 
from src.components.dailog_enroll import enroll_dialog
from src.components.dialog_submit_assignment import submit_assignment_dialog
from src.components.dailog_view_marks import view_marks_dialog

def student_dashboard():

    student_data = st.session_state.student_data

    student_id = student_data['student_id']

    c1, c2 = st.columns([4, 4], vertical_alignment='center', gap='large')
    with c1:
        header_dashboard()
    with c2:
            st.subheader(f"""Welcome, {student_data['name']}""")
            if st.button("Logout", type='secondary', key='login_back_btn',use_container_width=True):
             st.session_state['is_logged_in'] = False
             del st.session_state.student_data
             st.rerun()

    st.space()

    if "current_student_tab" not in st.session_state:
            st.session_state.current_student_tab = 'enrolled_subjects'

    tab1, tab2 = st.columns(2)

    with tab1:
            type1 = "primary" if st.session_state.current_student_tab == 'enrolled_subjects' else "tertiary"

            if st.button('Enrolled Subjects', type= type1,width='stretch',icon=':material/list_alt:'):
                  st.session_state.current_student_tab = 'enrolled_subjects'
                  st.rerun()

    with tab2:
            type2 = "primary" if st.session_state.current_student_tab == 'assignments_subjects' else "tertiary"

            if st.button('Your Assignments',type= type2,width='stretch',icon=':material/book_ribbon:'):
                  st.session_state.current_student_tab = 'assignments_subjects'
                  st.rerun()

    if st.session_state.current_student_tab == "enrolled_subjects":
            enrolled_subjects()

    if st.session_state.current_student_tab == "assignments_subjects":
            assignments_subjects()

    st.divider()

    footer_dashboard()

def enrolled_subjects():

    student_data = st.session_state.student_data
    student_id = student_data['student_id']

    c1, c2 =st.columns(2)
    with c1:
        st.header('Your Enrolled Subjects')
        
    with c2:
        if st.button('Enroll in Subject', type='secondary', width='stretch'):
            enroll_dialog()

    st.divider()

    with st.spinner('Loading your enrolled subjects..'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    if not subjects:
        st.info("You have no enrolled subjects")
        return
    stats_map = {}

    for log in logs:
        sid = log['subject_id']

        if sid not in stats_map:
            stats_map[sid] = {"total":0, "attended": 0}

        stats_map[sid]['total'] +=1

        if log.get('is_present'):
            stats_map[sid]['attended'] += 1


    cols = st.columns(2)

    for i, sub_node in enumerate(subjects):
        sub = sub_node["subjects"]
        sid = sub["subject_id"]

        stats = stats_map.get(sid, {"total": 0, "attended": 0})

        def unenroll_button(subject=sub, subject_id=sid):
            if st.button(
                "Unenroll from this course",
                key=f"unenroll_{subject_id}",
                type="tertiary",
                width="stretch",
                icon=":material/delete_forever:",
            ):
                unenroll_student_to_subject(student_id, subject_id)

                st.toast(
                    f'Unenrolled from {subject["name"]} successfully!'
                )

                st.rerun()

        with cols[i % 2]:
            subject_card(
                name=sub["name"],
                code=sub["subject_code"],
                section=sub["section"],
                stats=[
                    ("📅", "Total", stats["total"]),
                    ("✅", "Attended", stats["attended"]),
                ],
                footer_callback=unenroll_button,
            )

def assignments_subjects():

    student_id = st.session_state.student_data["student_id"]

    st.divider()
    
    st.header("📚 Assignments")
    with st.spinner('Loading your Assignments subjects..'):
     assignments = get_student_assignments(student_id)
    if not assignments:
        st.info("No assignments available.")
        return

    for assignment in assignments:

        submitted = has_submitted_assignment(
            assignment["assignment_id"],
            student_id
        )

        with st.container(border=True):
            st.markdown(f"**📚 Title:** {assignment['assignment_title']}")
            st.markdown(
    f"**📚 Subject:** {assignment['subject_name']} &nbsp;&nbsp;&nbsp;&nbsp; "
    f"**🆔 Subject Code:** {assignment['subject_code']} &nbsp;&nbsp;&nbsp;&nbsp; "
    f"**🏆 Max Marks:** {assignment['max_marks']}",
    unsafe_allow_html=True
    )

            given_date = assignment["created_at"]
            
            submission_date = assignment["submission_date"]

            st.markdown(
    f"**📅 Given Date:** {given_date} &nbsp;&nbsp;&nbsp;&nbsp; **📤 Submission Date:** {submission_date}",
    unsafe_allow_html=True
    )
            

            if submitted:
                st.success("✅ You have submitted this assignment successfully.")
            else:
                st.warning("⚠️ You have not submitted this assignment. Submit it as soon as possible, otherwise 0 marks may be awarded.")

            col1, col2 = st.columns(2)

            with col1:
                st.link_button(
                    "👁 View",
                    assignment["assignment_image"],
                    use_container_width=True
                )

            with col2:
                if submitted:
                 if st.button(
                 "📊 View Marks",
                 key=f"marks_{assignment['assignment_id']}",
                 use_container_width=True):
                     view_marks_dialog(assignment)
                else:
                     if st.button(
                "📤 Submit",
                key=f"submit_{assignment['assignment_id']}",
                use_container_width=True ):
                        submit_assignment_dialog(assignment["assignment_id"],student_id )

def student_screen():
    
    style_toolbar()
    style_background_dashboard()

    if "student_data" in st.session_state:
        student_dashboard()
        return


    c1, c2 = st.columns([4, 2], vertical_alignment='center', gap='xxlarge')

    with c1:
        header_dashboard()

    with c2:
        if st.button("Go back to Home", type='secondary', key='login_back_btn'):
             st.session_state['login_type'] = None
             st.rerun()

    st.markdown(
        "<h2 style='text-align:center; color:black;'>Student Login using FaceID</h2>",
        unsafe_allow_html=True
    )
    st.space()
    st.space()
    show_registration = False

    photo_source = st.camera_input("Position your face in center")
    if photo_source:
        img = np.array(Image.open(photo_source))
        with st.spinner('AI is scanning..'):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0:
                st.warning('Face not found!')

            elif num_faces > 1:
                st.warning('Multiple faces found!')
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_student = get_all_students()
                    student = next((s for s in all_student if s['student_id'] == student_id),None)

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data= student
                        st.toast(f"Welcome back {student['name']}")
                        import time
                        time.sleep(1)
                        st.rerun()

                else:
                    st.info('Face not recognized! You might be a new student.')
                    show_registration = True

    if show_registration:
        with st.container(border=True):
            st.header('Register a new Profile')
            new_name = st.text_input("Enter your name", placeholder='Abhisek Verma')
            st.subheader("Voice Enrollment for Voice Attendance")
            audio_data = None

            try:
                audio_data = st.audio_input('Record a short phase like I am present , My name is Anurag')
            except Exception as e:
                st.error('Audio Data failed')

            if st.button('Create Account',type='primary'):

                if new_name:
                 with st.spinner("Creating profile..."):
                    img = np.array(Image.open(photo_source))
                    encodings = get_face_embeddings(img)

                    if encodings:
                        face_emb = encodings[0].tolist()

                        voice_emb = None
                        if audio_data:
                            voice_emb = get_voice_embeddings(audio_data.read())
                            response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)

                        if response_data:
                            train_classifier()
                            st.session_state.is_logged_in = True
                            st.session_state.user_role = 'student'
                            st.session_state.student_data= response_data[0]
                            st.toast(f'Profile Created! Hi {new_name}')
                            import time
                            time.sleep(1)
                            st.rerun()

                    else:
                        st.error('Could not capture your facial features for registration')
                else:
                 st.warning('Please enter your name!')

    st.divider()
    footer_dashboard()
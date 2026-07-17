import streamlit as st
from src.database.db import create_assignment, get_teacher_subjects

@st.dialog("Create New Assignment")
def create_assignment_dialog(teacher_id):

    st.write("Enter assignment details")

    subjects = get_teacher_subjects(teacher_id)

    if not subjects:
        st.warning("No subjects found.")
        return

    subject = st.selectbox(
        "Select Subject",
        subjects,
        format_func=lambda x: f"{x['subject_code']} - {x['name']}"
    )

    assignment_title = st.text_input(
        "Assignment Title",
        placeholder="Assignment 1"
    )

    max_marks = st.number_input(
        "Maximum Marks",
        min_value=1,
        value=100
    )

    submission_date = st.date_input("Date of Submission")

    assignment_image = st.file_uploader(
    "Upload Assignment Image",
    type=["png", "jpg", "jpeg"]
    )

    if st.button(
        "Create Assignment",
        type="primary",
        use_container_width=True
    ):

        if assignment_title and assignment_image:

            try:
                create_assignment(
                teacher_id=teacher_id,
                subject_id=subject["subject_id"],
                assignment_title=assignment_title,
                max_marks=max_marks,
                assignment_image=assignment_image,
                submission_date= submission_date
            )

                st.toast("Assignment created successfully!")
                st.rerun()

            except Exception as e:
                st.error(f"Error: {e}")

        else:
            st.warning("Please fill all the required fields.")
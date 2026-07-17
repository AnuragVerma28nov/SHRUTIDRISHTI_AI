import streamlit as st
from src.database.db import submit_assignment


@st.dialog("Submit Assignment")
def submit_assignment_dialog(assignment_id, student_id):

    st.write("Upload your assignment in PDF format.")
    assignment_title = st.text_input(
        "Assignment Title",
        placeholder="Assignment 1"
    )
    pdf = st.file_uploader(
        "Choose PDF",
        type=["pdf"]
    )
    
    if st.button("Submit Assignment", type="primary", use_container_width=True):
        
        if pdf is None:
            st.warning("Please select a PDF.")
            return

        try:
            submit_assignment(
                assignment_id=assignment_id,
                student_id=student_id,
                pdf_file=pdf,
                assignment_title=assignment_title
            )

            st.toast("Assignment submitted successfully!")
            st.rerun()

        except Exception as e:
            st.error(f"Error: {e}")
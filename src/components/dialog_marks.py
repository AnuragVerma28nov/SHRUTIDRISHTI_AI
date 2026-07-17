import streamlit as st
from src.database.db import update_assignment_marks


@st.dialog("📝 Award Marks")
def marks_dialog(submission_id, student_name):

    st.write(f"**Student:** {student_name}")

    marks = st.number_input(
        "Obtained Marks",
        min_value=0,
        max_value=100,
        step=1
    )

    remark = st.text_area(
        "Remark",
        placeholder="Excellent work..."
    )

    if st.button(
        "Save Marks",
        type="primary",
        use_container_width=True
    ):

        update_assignment_marks(
            submission_id,
            marks,
            remark
        )

        st.toast("Marks Updated Successfully")
        st.rerun()
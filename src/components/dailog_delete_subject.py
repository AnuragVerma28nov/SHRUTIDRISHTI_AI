import streamlit as st
from src.database.db import delete_subject


@st.dialog("Delete Subject")
def delete_subject_dialog(subject):

    st.warning(
        f"Are you sure you want to delete '{subject['name']}'?"
    )

    st.error(
        "This will remove all attendance records, students and subject data."
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "Yes, Delete",
            key=f"confirm_delete_{subject['subject_id']}"
        ):

            success = delete_subject(subject['subject_id'])

            if success:
                st.success("Subject deleted successfully.")
                st.rerun()
            else:
                st.error("Failed to delete subject.")

    with col2:
        st.button("Cancel")
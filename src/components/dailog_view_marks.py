import streamlit as st
from src.database.db import get_submission_details


@st.dialog("📊 Assignment Result")
def view_marks_dialog(assignment):

    submission = get_submission_details(
        assignment["assignment_id"],
        st.session_state.student_data["student_id"]
    )

    st.subheader(assignment["assignment_title"])
    st.markdown(
        f"**📚 Subject:** {assignment['subject_name']} &nbsp;&nbsp;&nbsp;&nbsp; "
        f"**🆔 Subject Code:** {assignment['subject_code']}",
        unsafe_allow_html=True
    )

    st.write(
        f"**📅 Submitted On:** {submission['submitted_at'][:10]}"
    )

    if submission["obtained_marks"] is None:
        st.info("⏳ Your assignment has not been checked yet.")
        
    else:
        st.success(
            f"🏆 Obtained Marks : {submission['obtained_marks']} / {assignment['max_marks']}"
        )

    st.write(
        f"**💬 Remark:** {submission['remark'] or 'No remark'}"
    )
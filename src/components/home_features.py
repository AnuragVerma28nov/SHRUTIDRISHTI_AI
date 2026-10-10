import streamlit as st

def home_feature():

    st.subheader("✨ Key Features")

    student_col, teacher_col = st.columns(2, gap="large")

    with student_col:
        st.markdown("""
    ### 👨‍🎓 Student Portal

    - 📷 Face Registration
    - 🎤 Voice Registration
    - 📚 Enroll Subjects
    - 📖 View Attendance
    - 📝 Submit Assignments
    - 📊 View Marks & Remarks
    - 🔍 Search Subjects
    """,)

    with teacher_col:
        st.markdown("""
    ### 👨‍🏫 Teacher Portal

    - 📚 Create & Manage Subjects
    - 🔗 Share Subject QR Codes
    - 📷 Bulk Face Attendance
    - 🎤 Voice Attendance
    - 📈 Attendance Analytics
    - 📝 Create Assignments
    - ✅ AI Evaluate Submissions 
    - 💯 Award Marks & Feedback
    """)


    
    

    
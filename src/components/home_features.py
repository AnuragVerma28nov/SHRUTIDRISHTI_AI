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

    st.subheader("🛠 Technology Stack")

    tech1, tech2, tech3 = st.columns(3)

    with tech1:
        st.markdown("""
    ### Frontend
    - Streamlit
    - HTML
    - CSS
    - JS
    """)

    with tech2:
        st.markdown("""
    ### Backend
    - Supabase
    - PostgreSQL
    - Supabase Storage
    - Flask
    """)

    with tech3:
        st.markdown("""
    ### AI & ML
    - OpenCV
    - face_recognition
    - Resemblyzer
    - NumPy,Pandas
    - scikit-learn
    """)
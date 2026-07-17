import streamlit as st
from src.components.header import home_header, header_dashboard
from src.components.footer import home_footer
from src.ui.base_layout import style_toolbar, style_background_home

def home_screen():  
    home_header()
    st.space()
    style_toolbar()
    style_background_home()

    col1, col2 = st.columns(2,gap="large")

    with col1:
        st.header("I'm Student")
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width= 120)
        if st.button('Student Portal',type = 'primary',icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type'] = 'student'
            st.rerun()

    with col2:
        st.header("I'm Teacher")
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width= 145)
        if st.button('Teacher Portal',type = 'primary',icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type'] = 'teacher'
            st.rerun() 

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

    st.divider()
    home_footer()
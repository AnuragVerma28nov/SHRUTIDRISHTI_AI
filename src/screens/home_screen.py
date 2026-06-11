import streamlit as st
from src.components.home_header import home_header
from src.ui.style_layout import style_background_home
from src.ui.style_layout import style_toolbar
from src.ui.style_layout import style_background_dashboard

def home_screen():  
    home_header()
    style_toolbar()
    style_background_home()

    col1, col2 = st.columns(2)
    with col1:
        if st.button('Teacher Portal'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()
    with col2:
        if st.button('Student Portal'):
            st.session_state['login_type'] = 'student'
            st.rerun()

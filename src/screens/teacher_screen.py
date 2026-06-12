import streamlit as st
from src.ui.style_layout import style_toolbar, style_background_dashboard

from src.components.header import header_dashboard


def teacher_screen():
    style_toolbar()
    style_background_dashboard()
    teacher_login()


def teacher_login():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='large')

    with c1:
        header_dashboard()

    with c2:
        st.button(
            "Go back to Home",
            type='secondary',
            key='login_back_btn'
        )
    st.markdown(
        "<h2 style='text-align:center; color:black;'>Teacher Login using Password</h2>",
        unsafe_allow_html=True
    )
    teacher_name = st.text_input("Enter Username",placeholder='username')
    teacher_pass = st.text_input("Enter Password",placeholder='********')


def teacher_register():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='large')

    with c1:
        header_dashboard()

    with c2:
        st.button(
            "Go back to Home",
            type='secondary',
            key='register_back_btn'
        )

    st.markdown(
        "<h2 style='text-align:center;'>Register your Teacher Profile</h2>",
        unsafe_allow_html=True
    )
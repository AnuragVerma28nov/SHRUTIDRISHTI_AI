import streamlit as st  
from src.ui.base_layout import style_toolbar, style_background_dashboard
from src.components.header import header_dashboard
from src.components.footer import teacher_footer


def teacher_screen():
    style_toolbar()
    style_background_dashboard()

    if 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == "login":
         teacher_login()
    elif st.session_state.teacher_login_type == "register":
         teacher_register()

def teacher_login():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')

    with c1:
        header_dashboard()

    with c2:
        if st.button("Go back to Home", type='secondary', key='login_back_btn'):
             st.session_state['login_type'] = None
             st.rerun()

    st.markdown(
        "<h2 style='text-align:center; color:black;'>Teacher Login using Password</h2>",
        unsafe_allow_html=True
    )

    st.space()
    st.space()

    teacher_name = st.text_input("Enter Username",placeholder='@abhisek')

    teacher_pass = st.text_input("Enter Password",type='password', placeholder='password')

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:st.button("Login Now",icon=':material/passkey:', icon_position='left',width='stretch', type='primary')
            
    with btnc2:
        if st.button("Register Instead",icon=':material/passkey:', icon_position='left',width='stretch'):
             st.session_state.teacher_login_type = 'register'

    teacher_footer()

def teacher_register():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')

    with c1:
        header_dashboard()

    with c2:
        if st.button("Go back to Home", type='secondary', key='register_back_btn'):
             st.session_state['login_type'] = None
             st.rerun()

    st.markdown(
                "<h2 style='text-align:center; color:black;'>Register your Teacher Profile</h2>",
        unsafe_allow_html=True
    )

    st.space()
    st.space()

    teacher_username = st.text_input("Enter Username",placeholder='@abhisek')

    teacher_name = st.text_input("Enter Name",placeholder='Abhisek Roy')

    teacher_pass = st.text_input("Enter Password",type='password', placeholder='Password')

    teacher_pass_confirm = st.text_input("Enter Confirm Password",type='password', placeholder='Confirm Password')

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
            st.button(
            "Register Now",
            icon=':material/passkey:', icon_position='left',width='stretch', type='primary'
        )
            
    with btnc2:
        if st.button("Login Instead",icon=':material/passkey:', icon_position='left',width='stretch'):
             st.session_state.teacher_login_type = 'login'

    teacher_footer()
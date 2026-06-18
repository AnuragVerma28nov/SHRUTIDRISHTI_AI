import streamlit as st  
from src.ui.base_layout import style_toolbar, style_background_dashboard
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.database.db import check_teacher_exists,teacher_login,create_teacher


def teacher_screen():
    style_toolbar()
    style_background_dashboard()
    if "teacher_data" in st.session_state:
          teacher_dashboard()

    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == "login":
         teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
         teacher_screen_register()

def teacher_dashboard():
      teacher_data = st.session_state.teacher_data
      st.header(f"""Welcome, {teacher_data['name']}""")
      
def login_teacher(username,password):
      if not username or not password:
            return False
      teacher = teacher_login(username,password)
      if teacher:
            st.session_state.user_role = 'teacher'
            st.session_state.teacher_data = teacher
            st.session_state.is_logged_in = True
            return True
      return False
      

def teacher_screen_login():
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

    teacher_username = st.text_input("Enter Username",placeholder='@abhisek')

    teacher_pass = st.text_input("Enter Password",type='password', placeholder='password')

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
            if st.button("Login Now",icon=':material/passkey:', icon_position='left',width='stretch', type='primary'):
                  if login_teacher(teacher_username,teacher_pass):
                        st.toast("Welcome back",icon="🎉")
                        import time
                        time.sleep(2)
                        st.rerun()   
                  else:
                        st.error("Invalid  ceredentials")         
    with btnc2:
        if st.button("Register Instead",icon=':material/passkey:', icon_position='left',width='stretch'):
             st.session_state.teacher_login_type = 'register'

    footer_dashboard()

def register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm ):
     if not teacher_username or not teacher_name or not teacher_pass:
          return False ,"All fields are must required!"
     if check_teacher_exists(teacher_username):
                    return False ,"Username is already exists."
     if teacher_pass != teacher_pass_confirm:
                    return False ,"Both password doesn't match"
     
     try:
           create_teacher(teacher_username,teacher_pass,teacher_name)
           return True,"Successfully created!Login now"
     except Exception as e:
            return False ,"Unexpected error! Try again"

def teacher_screen_register():
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
            if st.button("Register Now", icon=':material/passkey:', icon_position='left',width='stretch', type='primary'):
                 success, message = register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm )
                 if success:
                       st.success(message)     
                       import time
                       time.sleep(2)
                       st.session_state.teacher_login_type = 'login'
                       st.rerun()
                 else:
                  st.error(message)
            
    with btnc2:
        if st.button("Login Instead",icon=':material/passkey:', icon_position='left',width='stretch'):
             st.session_state.teacher_login_type = 'login'

    footer_dashboard()
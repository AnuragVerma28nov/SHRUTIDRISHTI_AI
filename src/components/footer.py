import streamlit as st

def home_footer():
    logo_url = "https://avatars.githubusercontent.com/u/181570564?v=4&size=64"

    st.markdown(f"""
                <div style='display:flex; gap:6px; items-align:center; justify-content:center; margin-top:2rem;'>
                <p style='font-weight:bold; color: white;'>Developed by:- Anurag Verma</p>
                <img src = '{logo_url}' style='max-height:25px;'/>                
                </div> 
                <style>

                </style>
                    """
                ,unsafe_allow_html  = True)
    
def teacher_footer():
    logo_url = "https://avatars.githubusercontent.com/u/181570564?v=4&size=64"

    st.markdown(f"""
                <div style='display:flex; gap:6px; items-align:center; justify-content:center; margin-top:2rem;'>
                <p style='font-weight:bold; color: black;'>Developed by:- Anurag Verma</p>
                <img src = '{logo_url}' style='max-height:25px;'/>                
                </div> 
                <style>

                </style>
                    """
                ,unsafe_allow_html  = True)

    
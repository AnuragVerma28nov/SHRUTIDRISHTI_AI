import streamlit as st

def home_header():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
                <div style='display:flex; flex-direction:column; align-items:center; justify-content:center; margin-top:30px; margin-botton:30px; '>
                <img src = '{logo_url}' style='height:100px; '/>
                <h1 style='text-algin:center; color:#E0E3FF'>SNAP</br>CLASS</h1>
                </div> 
                <style>

                </style>

                    """
                ,unsafe_allow_html  = True)

def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
                <div style='display:flex; align-items:center; justify-content:center; gap:10px; '>
                <img src = '{logo_url}' style='height:85px; '/>
                <h2 style='text-algin:left; color:#5865F2'> SNAP</br>CLASS</h2>
                </div> 
                <style>

                </style>

                    """
                ,unsafe_allow_html  = True)

    


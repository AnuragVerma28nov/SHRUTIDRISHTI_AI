import streamlit as st

def home_header():
    logo_url = "https://i.ibb.co/cKxnP697/favicon.png"

    st.markdown(f"""
                <div style='display:flex; margin-top:0px; align-items:center; justify-content:center; gap:10px; '>
                <img src = '{logo_url}' style='height:150px; border-radius:12px;
                 box-shadow:0 4px 10px rgba(0,0,0,0.2);
               '/>
                <h1 style='text-algin:left; color:#FFFDD0'>ShrutiDrishti AI</h1>
                </div> 
                    """
                ,unsafe_allow_html  = True)

def header_dashboard():
    logo_url = "https://i.ibb.co/cKxnP697/favicon.png"

    st.markdown(f"""
                <div style='display:flex; margin-top:0px; align-items:center; justify-content:center; gap:10px; '>
                <img src = '{logo_url}' style='height:85px; border-radius:12px;
                 box-shadow:0 4px 10px rgba(0,0,0,0.2);
             '/>
                <h2 style='text-algin:left; color:#5865f2'>ShrutiDrishti</br>AI</h2>
                </div> 
                

                    """
                ,unsafe_allow_html  = True)

    
import streamlit as st

def home_footer():
    logo_url = "https://i.ibb.co/cKxnP697/favicon.png"

    st.markdown(f"""
                <div style='display:flex; gap:6px; items-align:center; justify-content:center; margin-top:2rem;'>
                <p style='font-weight:bold; color: black;'>Developed by 👤 Anurag Verma | Powered by ShrutiDrishti AI<p>
                <img src = '{logo_url}' style='max-height:25px;border-radius:10px;'/>                
                </div> 
                    """
                ,unsafe_allow_html  = True)
    
def footer_dashboard():
    logo_url = "https://i.ibb.co/cKxnP697/favicon.png"

    st.markdown(f"""
                <div style='display:flex; gap:6px; items-align:center; justify-content:center; margin-top:2rem;'>
                <p style='font-weight:bold; color: black;'>Developed by 👤 Anurag Verma | Powered by ShrutiDrishti AI<p>
                <img src = '{logo_url}' style='max-height:25px;border-radius:10px;'/>                

                </div> 
                    """
                ,unsafe_allow_html  = True)

    
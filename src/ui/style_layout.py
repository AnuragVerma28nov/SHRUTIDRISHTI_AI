import streamlit as st

# Hide top toolbar
def style_toolbar():
    st.markdown("""
                
                <style>
            /*for headings*/    
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');

            /*for fonts*/    
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');

                #MainMenu, footer, header{
                visibility: hidden;
                }

                .block-container{
                padding-top:1.5rem;
                }

                h1{
                font-family:'Climate Crisis',sans-serif !important;
                font-size:305 rem !important;
                line-height:1.1 !important;
                margin-bottom:0 rem !important; 
                }

                h2{
                font-family:'Climate Crisis',sans-serif !important;
                font-size:305 rem !important;
                line-height:0.9 !important;
                margin-bottom:0 rem !important; 
                }

                h3,h4,p{
                font-family:'Outfit',sans-serif;
                }

                button{
                border-radius:1.5rem !important;
                background-color:#f258e3 !important; 
                color:white !important;
                padding:10px 20px !important;
                border:none !important;
                transition: transform 0.25s ease-in-out !important;
                }
                
                button[kind="Secondary"]{
                border-radius:1.5rem !important;
                background-color:#EB4459E !important; 
                color:white !important;
                padding:10px 20px !important;
                border:none !important;
                transition: transform 0.25s ease-in-out !important;
                }

                button[kind="tertiary"]{
                border-radius:1.5rem !important;
                background-color:black !important; 
                color:white !important;
                padding:10px 20px !important;
                border:none !important;
                transition: transform 0.25s ease-in-out !important;
                }
                button:hover{
                transform: scale(1.05);
                }

                </style>

                    """
                ,unsafe_allow_html  = True)

# Home Screen
def style_background_home():
    st.markdown("""
                
                <style>
                .stApp{
                background:#5865f2 !important;
                }
                </style>

                    """
                ,unsafe_allow_html  = True)

# Teacher Screen
def style_background_dashboard():
    st.markdown("""
                
                <style>
                .stApp{
                background:##E0E3FF !important;
                }
                </style>

                    """
                ,unsafe_allow_html  = True)
    


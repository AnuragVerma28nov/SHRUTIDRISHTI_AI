import streamlit as st

# Hide top toolbar
def style_toolbar():
    st.markdown("""
    <style>

    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&family=Outfit:wght@100..900&display=swap');

    /* Hide Streamlit UI elements */
    # MainMenu,
    # footer,
    # header {
    #     visibility: hidden;
    # }

    .block-container {      
        padding-top: 1.5rem;
    }

    /* Headings */
    h1 {
        font-family: 'Climate Crisis', sans-serif !important;
        font-size: 3.5rem !important;
        line-height: 1.1 !important;
        margin-bottom: 0rem !important;
    }

    h2 {
        font-family: 'Climate Crisis', sans-serif !important;
        font-size: 1.5rem !important;
        line-height: 0.9 !important;
        margin-bottom: 0rem !important;
    }

    /* Body text */
    h3,
    h4,
    p {
        font-family: 'Outfit', sans-serif !important;
    }

    /* Default Button */
    button {
        border-radius: 1.5rem !important;
        background-color: #f258e3 !important;
        color: white !important;
        padding: 10px 20px !important;
        border: none !important;
        transition: transform 0.25s ease-in-out !important;
    }

    /* Secondary Button */
    button[kind="secondary"] {
        border-radius: 1.5rem !important;
        background-color: #EB4459 !important;
        color: white !important;
        padding: 10px 20px !important;
        border: none !important;
        transition: transform 0.25s ease-in-out !important;
    }

    /* Tertiary Button */
    button[kind="tertiary"] {
        border-radius: 1.5rem !important;
        background-color: black !important;
        color: white !important;
        padding: 10px 20px !important;
        border: none !important;
        transition: transform 0.25s ease-in-out !important;
    }

    button:hover {
        transform: scale(1.05);
    }

    </style>
    """, unsafe_allow_html=True)


# Home Screen
def style_background_home():
    st.markdown("""
    <style>

    .stApp {
        background: #5865f2 !important;
    }

    div[data-testid="stColumn"] {
        background-color: #E0E3FF !important;
        padding: 2.5rem !important;
        color: black;
        border-radius: 5rem !important;
    }

    </style>
    """, unsafe_allow_html=True)


# Dashboard Screen
def style_background_dashboard():
    st.markdown("""
    <style>

    .stApp {
        background: #E0E3FF !important;
    }

    </style>
    """, unsafe_allow_html=True)
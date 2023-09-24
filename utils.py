import streamlit as st

def hide_streamlit_style(): 
    payload = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
    st.markdown(payload, unsafe_allow_html=True)
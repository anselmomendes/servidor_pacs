import os
import streamlit as st

# Titulos e fivicon
st.set_page_config(page_title="Systen PACS",
                   page_icon="⚕️",
                   layout="wide")

# Remove botão deploy e opções de configuração do menu
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/5523/5523656.png", width=280)
    st.divider()                   

st.markdown("# Systen PACS")


import os
import streamlit as st
from streamlit_keycloak import login


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
    st.image("https://dataway.info/wp-content/uploads/2023/02/dtw_lg_500x180-removebg.png", width=280)
    st.divider()                   

st.markdown("# Dataway")


st.title("Keycloak example")
keycloak = login(
    url="http://localhost/keycloak/",
    realm="orthanc",
    client_id="orthanc",
    auto_refresh=True,
    init_options={"checkLoginIframe": False},
    custom_labels={
        "labelButton": "Sign in",
        "labelLogin": "Please sign in to your account.",
        "errorNoPopup": "Unable to open the authentication popup. Allow popups and refresh the page to proceed.",
        "errorPopupClosed": "Authentication popup was closed manually.",
        "errorFatal": "Unable to connect to Keycloak using the current configuration."   
    }
)

if keycloak.authenticated:
    st.subheader(f"Welcome {keycloak.user_info['preferred_username']}!")
    st.write(f"Here is your user information:")
    st.write(asdict(keycloak))


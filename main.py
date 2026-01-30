import streamlit as st
from streamlit_option_menu import option_menu


with st.sidebar:
    data = option_menu(
        menu_title = "My Project",
        options = [
            "Home",
            "About",
            "Contact",
        ]
    )

import streamlit as st

st.set_page_config(page_title="Settings", page_icon="⚙", layout="wide")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("⚙ Settings")

theme = st.selectbox(
    "Theme",
    [
        "Dark",
        "Light"
    ]
)

notifications = st.checkbox(
    "Enable Notifications",
    value=True
)

voice = st.checkbox(
    "Enable Voice Assistant"
)

st.button("Save Settings")

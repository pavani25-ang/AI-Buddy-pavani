import streamlit as st
from utils import generate_response

st.set_page_config(page_title="Learn", page_icon="📖", layout="wide")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📖 Learn with AI")

topic = st.text_input("Enter Topic")

activity = st.radio(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Summary",
        "Teach Step-by-Step"
    ],
    horizontal=True
)

if st.button("🚀 Generate"):

    if topic:

        with st.spinner("Generating..."):

            answer = generate_response(topic, activity)

        st.markdown(answer)

    else:

        st.warning("Enter Topic")

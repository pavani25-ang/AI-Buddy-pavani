import streamlit as st
from utils import generate_response

st.set_page_config(page_title="Quiz", page_icon="🧠", layout="wide")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🧠 AI Quiz Generator")

topic = st.text_input("Quiz Topic")

if st.button("Generate Quiz"):

    if topic:

        with st.spinner("Creating Quiz..."):

            quiz = generate_response(topic, "Generate Quiz")

        st.markdown(quiz)

    else:

        st.warning("Enter Topic")

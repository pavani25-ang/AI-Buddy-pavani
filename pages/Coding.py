import streamlit as st

st.set_page_config(page_title="Coding", page_icon="💻", layout="wide")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("💻 Coding Assistant")

language = st.selectbox(
    "Programming Language",
    [
        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript"
    ]
)

question = st.text_area("Ask your coding question")

if st.button("Get Help"):

    st.success("🚀 Coding Assistant will be added in the next update.")

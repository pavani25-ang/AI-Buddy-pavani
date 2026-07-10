import streamlit as st

st.set_page_config(page_title="Progress", page_icon="📈", layout="wide")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📈 Learning Progress")

st.metric("Topics Learned", "48")

st.metric("Quiz Score", "91%")

st.metric("Current Streak", "12 Days")

st.metric("XP", "1240")

st.divider()

st.subheader("Weekly Progress")

st.progress(80)

st.success("Excellent Progress 🚀")

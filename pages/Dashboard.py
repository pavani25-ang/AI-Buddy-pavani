import streamlit as st

st.set_page_config(page_title="Dashboard", page_icon="🏠", layout="wide")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🏠 Dashboard")

st.write("Welcome back, Pavani 👋")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📚 Topics", "48", "+3")

with col2:
    st.metric("🔥 Streak", "12 Days", "+1")

with col3:
    st.metric("🧠 Quizzes", "20", "+2")

with col4:
    st.metric("🏆 XP", "1240", "+120")

st.divider()

st.subheader("📈 Recent Activity")

st.success("✅ Learned Machine Learning")

st.info("📖 Completed Java Collections")

st.warning("🧠 Quiz on DBMS Tomorrow")

st.divider()

st.subheader("🎯 Today's Goal")

st.progress(65)

st.write("65% Completed")

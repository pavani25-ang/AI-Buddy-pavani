import streamlit as st
from streamlit_option_menu import option_menu

from utils import generate_response


# ---------------------
# Page Config
# ---------------------

st.set_page_config(
    page_title="AI Buddy Pavani",
    page_icon="🤖",
    layout="wide"
)


# ---------------------
# Load CSS
# ---------------------

with open("styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


# ---------------------
# Sidebar
# ---------------------

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/4712/4712109.png",
        width=120
    )

    st.markdown("## 🤖 AI Buddy")

    selected = option_menu(
        "",
        [
            "Dashboard",
            "Learn",
            "Quiz",
            "Coding",
            "Progress",
            "Settings"
        ],
        icons=[
            "house",
            "book",
            "patch-question",
            "code-slash",
            "graph-up",
            "gear"
        ],
        default_index=0
    )


# ---------------------
# Header
# ---------------------

st.markdown(
    "<div class='main-title'>🤖 AI Buddy Pavani</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Your Personal AI Learning Assistant</div>",
    unsafe_allow_html=True
)


# ---------------------
# Dashboard Cards
# ---------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        "<div class='metric'>📚<br>Topics<br><h2>48</h2></div>",
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        "<div class='metric'>🔥<br>Streak<br><h2>12</h2></div>",
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        "<div class='metric'>🧠<br>Quizzes<br><h2>20</h2></div>",
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        "<div class='metric'>🏆<br>XP<br><h2>1240</h2></div>",
        unsafe_allow_html=True
    )

st.write("")

# ---------------------
# Input
# ---------------------

topic = st.text_input(
    "🔍 What do you want to learn today?",
    placeholder="Example: Artificial Intelligence"
)

activity = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Summary",
        "Generate Quiz",
        "Teach Step-by-Step"
    ]
)

if st.button("🚀 Generate"):

    if topic == "":
        st.warning("Please enter a topic.")

    else:

        with st.spinner("🤖 AI is Thinking..."):

            answer = generate_response(topic, activity)

        st.markdown(
            "<div class='response'>"
            + answer.replace("\n", "<br>")
            + "</div>",
            unsafe_allow_html=True
        )

import streamlit as st
from streamlit_option_menu import option_menu
from utils import generate_response

# ---------------------
# Page Config
# ---------------------

st.set_page_config(
    page_title="AI Learning Buddy - Pavani",
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
     "assets/logo.png",
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

# ---------------------
# Generate Response
# ---------------------

if st.button("🚀 Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        with st.spinner("🤖 AI is Thinking..."):

            answer = generate_response(topic, activity)

        st.markdown(
            f"<div class='response'>{answer.replace(chr(10), '<br>')}</div>",
            unsafe_allow_html=True
        )

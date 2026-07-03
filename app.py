
import streamlit as st
import google.generativeai as genai

# ----------------------------
# Gemini API
# ----------------------------


genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model=genai.GenerativeModel("gemini-2.5-flash")

# ----------------------------
# Streamlit UI
# ----------------------------

st.set_page_config(page_title="AI Buddy Pavani",page_icon="🤖")

st.title("🤖 AI Buddy Pavani")

st.write("Your Personal AI Learning Assistant")

topic=st.text_input(
    "Enter Topic",
    placeholder="Example: Artificial Intelligence"
)

activity=st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Summary",
        "Generate Quiz",
        "Teach Step-by-Step"
    ]
)

if st.button("Generate"):

    if topic=="":

        st.warning("Please enter a topic.")

    else:

        if activity=="Explain Concept":

            prompt=f"""
Explain {topic} in simple language as if teaching a 15-year-old student.
Use easy words.
Use one analogy.
Keep it under 150 words.
"""

        elif activity=="Real-Life Example":

            prompt=f"""
Give one real-life example of {topic}.
Explain how it works in simple language.
"""

        elif activity=="Summary":

            prompt=f"""
Summarize {topic} in five simple bullet points.
"""

        elif activity=="Generate Quiz":

            prompt=f"""
Create five multiple-choice questions on {topic}.

Each question must contain

A)
B)
C)
D)

After every question provide

Correct Answer

Short Explanation
"""

        elif activity=="Teach Step-by-Step":

            prompt=f"""
You are a friendly teacher.

Teach {topic} step by step.

Start from beginner level.

Explain one concept at a time.

Ask one question at the end.
"""

        with st.spinner("AI is Thinking..."):

            response=model.generate_content(prompt)

            st.success("Done!")

            st.write(response.text)

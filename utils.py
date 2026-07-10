import google.generativeai as genai
import streamlit as st


# -------------------------
# Configure Gemini
# -------------------------
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])


model = genai.GenerativeModel("gemini-2.5-flash")


def get_prompt(topic, activity):

    prompts = {

        "Explain Concept": f"""
Explain {topic} in very simple language.

Structure:

1. Definition

2. Key Points

3. Easy Example

4. Real Life Application

5. Interview Tip

Keep under 250 words.
""",

        "Real-Life Example": f"""
Give a real-world example of {topic}.

Explain step-by-step.

Keep it beginner friendly.
""",

        "Summary": f"""
Summarize {topic}.

Use bullet points.

Maximum 10 points.
""",

        "Generate Quiz": f"""
Generate 5 MCQs about {topic}.

Each question should contain

A)
B)
C)
D)

Then give

Correct Answer

Explanation
""",

        "Teach Step-by-Step": f"""
Teach {topic} like a teacher.

Go from Beginner to Advanced.

Explain one step at a time.

Ask one question at the end.
"""
    }

    return prompts.get(activity, "")


def generate_response(topic, activity):

    prompt = get_prompt(topic, activity)

    response = model.generate_content(prompt)

    return response.text

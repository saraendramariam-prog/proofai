import os

import streamlit as st
import ollama

# -----------------------------------
# PAGE SETTINGS
# -----------------------------------

st.set_page_config(
    page_title="ProofAI | Learn with Confidence",
    page_icon="🌿",
    layout="centered"
)

# -----------------------------------
# SAGE & CREAM DESIGN
# -----------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&display=swap');

h1 {
    font-family: 'Playfair Display', serif;
}


/* Main page */
.stApp {
    background-color: #F5F3E9;
    color: #344B3A;
}

/* Main content width and spacing */
.block-container {
    max-width: 800px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

/* Headings */
h1, h2, h3 {
    color: #344B3A !important;
    font-family: sans-serif;
}

/* Main title */
h1 {
    font-size: 2.8rem !important;
    font-weight: 750 !important;
    letter-spacing: -1.5px;
}

/* Normal text */
p, label, .stMarkdown {
    color: #52634F;
}

/* Input labels */
.stTextInput label,
.stTextArea label {
    color: #344B3A !important;
    font-weight: 600;
}

/* Question and working boxes */
.stTextInput input,
.stTextArea textarea {
    background-color: #FFFDF7 !important;
    color: #344B3A !important;
    border: 1px solid #D5DDCF !important;
    border-radius: 14px !important;
}

/* Focus effect */
.stTextInput input:focus,
.stTextArea textarea:focus {
    border-color: #647963 !important;
    box-shadow: 0 0 0 2px #DCE5D5 !important;
}

/* Main button */
.stButton > button {
    background-color: #647963 !important;
    color: white !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 0.75rem 1.2rem !important;
    font-weight: 650 !important;
    transition: all 0.2s ease;
    width: 100%;
}

/* Button hover */
.stButton > button:hover {
    background-color: #4F654E !important;
    color: white !important;
    transform: translateY(-1px);
}

/* Feedback and message boxes */
.stAlert {
    border-radius: 14px;
}

/* Divider */
hr {
    border-color: #DDE2D5;
}

/* Small footer text */
.footer {
    color: #819078;
    text-align: center;
    font-size: 0.85rem;
    padding-top: 2rem;
}

/* Hide the default Streamlit footer */
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# HEADER
# -----------------------------------

st.markdown(
    "<p style='font-size:14px; letter-spacing:3px; "
    "color:#71836A; font-weight:700;'>YOUR PERSONAL AI TUTOR</p>",
    unsafe_allow_html=True
)

st.title("ProofAI 🌿")

st.markdown(
    "### Show your working. Understand your answer."
)

st.write(
   "🌷Every mistake/failiure  is a step towards learning!🌷"
)

st.divider()

# -----------------------------------
# STUDENT INPUTS
# -----------------------------------

st.subheader(" Let's work through it")

question = st.text_input(
    "What is your question?",
    placeholder="e.g. How do I add fractions?"
)

work = st.text_area(
    "Show your work:",
    placeholder="Write your steps here. Don't worry about mistakes!",
    height=160
)

st.write("")

# -----------------------------------
# CHECK THE STUDENT'S WORK
# -----------------------------------

if st.button("🌿  Check My Work", use_container_width=True):

    if not question.strip():
        st.warning("Please enter your question!")

    elif not work.strip():
        st.warning("Please show your work!")

    else:

        prompt = f"""
You are ProofAI, a friendly, patient AI tutor for school students.

The student's question is:
{question}

The student's working is:
{work}

Your job:

1. Carefully understand the question before evaluating the work.
2. Check each step of the student's reasoning.
3. Identify which steps are correct and explain why.
4. If there is a mistake, clearly identify the first incorrect step.
5. Explain the mistake kindly without making the student feel bad.
6. Give a helpful hint before revealing a complete solution,
   whenever a hint would help the student learn.
7. Explain the correct method in simple, age-appropriate language.
8. If the work is correct, congratulate the student and explain why.
9. Never claim that work is correct unless you have checked it.
10. If the question or working is unclear, ask for clarification
    instead of guessing.
11. Use readable formatting and short paragraphs.
12. Do not invent steps that the student did not write.

Be accurate, encouraging, and educational.
Focus on helping the student understand, not just giving an answer.
"""

        try:
            with st.spinner("🌱 ProofAI is carefully checking your work..."):

                response = ollama.chat(
                    model="llama3.2",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

            feedback = response["message"]["content"]

            st.divider()

            st.markdown("## 🌿 Your learning feedback")

            st.markdown(
                "<div style='background-color:#FFFDF7; "
                "border:1px solid #DDE2D5; "
                "border-radius:16px; padding:22px;'>",
                unsafe_allow_html=True
            )

            st.markdown(feedback)

            st.markdown("</div>", unsafe_allow_html=True)

            st.caption(
                "Remember: understanding the method matters more "
                "than getting the answer right on your first try."
            )

        except Exception as e:
            st.error(
                "ProofAI couldn't respond. Please check that Ollama "
                "is running and the llama3.2 model is available."
            )
            st.caption(f"Technical details: {e}")

# -----------------------------------
# FOOTER
# -----------------------------------

st.markdown(
    "<div class='footer'>your little study space 🤍</div>",
    unsafe_allow_html=True
)


                
import streamlit as st
from ollama import Client

client = Client(host="http://localhost:11434")

st.set_page_config(
    page_title="Deep Ocean AI",
    layout="wide"
)

# --- Custom CSS: Deep Ocean Theme ---
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #0a2540 0%, #023e58 40%, #01161e 100%);
        color: #e0f7fa;
    }

    h1 {
        text-align: center;
        font-size: 3rem !important;
        background: linear-gradient(90deg, #4fd1ff, #8ec5fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        color: #7fdbff;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    .stTextArea textarea {
        background-color: black;
        color: white;
        border: 1px solid #2a9df4;
        border-radius: 12px;
        font-size: 1rem;
    }

    .stButton button {
        background: linear-gradient(90deg, #0077b6, #00b4d8);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.6em 2em;
        font-weight: 600;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .stButton button:hover {
        transform: scale(1.03);
        box-shadow: 0 0 15px #00b4d8;
    }

    .response-box {
        background-color: rgba(255, 255, 255, 0.06);
        border-left: 4px solid #00b4d8;
        border-radius: 10px;
        padding: 1.2rem;
        margin-top: 1rem;
        line-height: 1.6;
    }

    /* Bubble decorations */
    .bubble {
        position: fixed;
        bottom: -100px;
        opacity: 0.15;
        animation: rise 12s infinite ease-in;
        color: #7fdbff;
    }
    @keyframes rise {
        0%   { bottom: -100px; opacity: 0; }
        50%  { opacity: 0.2; }
        100% { bottom: 100%; opacity: 0; }
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1> Deep Ocean AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Dive into conversation with your local LLM</p>", unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])

with col1:
    prompt = st.text_area(" Enter your prompt:", height=200, placeholder="Ask the deep something...")

with col2:
    st.markdown("###  Tips")
    st.info("Keep prompts clear and specific for the best response from the depths.")

if st.button(" Generate Response"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt before diving in.")
    else:
        with st.spinner(" Surfacing an answer..."):
            response = client.chat(
                model="deepseek-r1:1.5b",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

        st.success(" Response Generated!")
        st.markdown(
            f"<div class='response-box'>{response['message']['content']}</div>",
            unsafe_allow_html=True
        )
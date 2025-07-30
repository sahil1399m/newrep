import streamlit as st
from streamlit_lottie import st_lottie
import requests
import google.generativeai as genai

# --- Gemini API Key (Do Not Edit This Block) ---
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error(f"Gemini API Key error: {e}")
    model = None

st.set_page_config(page_title="Sahil's Portfolio", page_icon="🚀", layout="wide")

# Function to load Lottie animation from a URL
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
lottie_hero = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_touohxv0.json")  # Rocket
lottie_about = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_gnb2nzzr.json")   # Developer
lottie_projects = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_u4yrau.json")  # Projects
lottie_chatbot = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_0yfsb3a1.json")  # Chatbot
lottie_footer = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_3rwasyjy.json")   # Thanks

# Hero Section
with st.container():
    st.subheader("Hi, I am Sahil 👋")
    st.title("Welcome to My Portfolio")
    st.write("Aspiring Developer | Innovator | Engineer @ VJTI")
    st_lottie(lottie_hero, height=300, key="hero")

# About Section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write(
            "I’m a second-year EXTC student at VJTI passionate about tech, AI, and building impactful projects. "
            "From robotics with ESP32 to AI-powered assistants — I love solving real-world problems."
        )
    with right_column:
        st_lottie(lottie_about, height=300, key="about")

# Projects Section
with st.container():
    st.write("---")
    st.header("My Projects")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("### 🔧 Face-Based Attendance System")
        st.write("Detects real-time proxy using facial recognition with OpenCV + ESP32 alert system.")
        st.write("### 🚗 Driver Drowsiness Detection")
        st.write("Monitors eye/yawn and alerts using buzzer and voice assistant.")
    with right_column:
        st_lottie(lottie_projects, height=300, key="projects")

# Chatbot Section
with st.container():
    st.write("---")
    st.header("🤖 Ask My AI Assistant")
    prompt = st.text_input("What would you like to ask?", "")
    if prompt and model:
        response = model.generate_content(prompt)
        st.success(response.text)
    elif not model:
        st.error("Model could not be initialized. Check API Key.")
    st_lottie(lottie_chatbot, height=300, key="chatbot")

# Footer Section
with st.container():
    st.write("---")
    left_col, right_col = st.columns(2)
    with left_col:
        st.title("✨ Thanks for Visiting!")
        st.write("This portfolio is built with Python, Streamlit, and love for innovation.")
    with right_col:
        st_lottie(lottie_footer, height=250, key="footer")

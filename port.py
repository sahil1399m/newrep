import streamlit as st
from streamlit_lottie import st_lottie
import requests
import google.generativeai as genai

# --- Page Config ---
st.set_page_config(page_title="Sahil's Portfolio", page_icon="🚀", layout="wide")

# --- Gemini API Key (Do Not Edit This Block) ---
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error(f"Gemini API Key error: {e}")
    model = None

# --- Function to Load Lottie Animation ---
def load_lottie_url(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None

# --- Load Animations ---
lottie_hero = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_touohxv0.json")
lottie_about = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_gnb2nzzr.json")
lottie_projects = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_u4yrau.json")
lottie_chatbot = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_0yfsb3a1.json")
lottie_footer = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_3rwasyjy.json")

# --- Hero Section ---
with st.container():
    st.subheader("Hi, I am Sahil Desai :wave:")
    st.title("A Student, Developer & Innovator")
    st.write("I am passionate about building projects that blend AI, electronics, and code.")
    if lottie_hero:
        st_lottie(lottie_hero, height=300, key="hero")
    else:
        st.warning("⚠️ Hero animation failed to load.")

# --- About Section ---
with st.container():
    st.write("---")
    st.header("About Me")
    st.write("I am a second-year EXTC student at VJTI, passionate about AI, embedded systems, and data science.")
    if lottie_about:
        st_lottie(lottie_about, height=300, key="about")
    else:
        st.warning("⚠️ About animation failed to load.")

# --- Projects Section ---
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("- Smart Distance Monitoring System using ESP32\n- Face-based Proxy Detection System\n- Driver Drowsiness Detection\n- Data Science Roadmap and Visualizations")
    if lottie_projects:
        st_lottie(lottie_projects, height=300, key="projects")
    else:
        st.warning("⚠️ Projects animation failed to load.")

# --- Chatbot Section ---
with st.container():
    st.write("---")
    st.header("Ask My AI Chatbot")
    user_prompt = st.text_input("Ask anything about me or my work:")
    if user_prompt and model:
        response = model.generate_content(user_prompt)
        st.success(response.text)
    elif user_prompt:
        st.error("Gemini model not loaded.")
    if lottie_chatbot:
        st_lottie(lottie_chatbot, height=300, key="chatbot")
    else:
        st.warning("⚠️ Chatbot animation failed to load.")

# --- Footer ---
with st.container():
    st.write("---")
    st.write("Connect with me on [GitHub](https://github.com/) | [LinkedIn](https://www.linkedin.com/)")
    if lottie_footer:
        st_lottie(lottie_footer, height=150, key="footer")
    else:
        st.warning("⚠️ Footer animation failed to load.")

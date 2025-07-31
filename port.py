import streamlit as st
from streamlit_lottie import st_lottie
import requests
import google.generativeai as genai

# --- Page Config ---
st.set_page_config(page_title="Sahil Desai | Portfolio", layout="wide", page_icon="💼")

# --- Theme Toggle ---
if "theme" not in st.session_state:
    st.session_state["theme"] = "light"

theme_toggle = st.toggle("🌙 Dark Mode", value=(st.session_state["theme"] == "dark"))
st.session_state["theme"] = "dark" if theme_toggle else "light"

# --- Apply Theme CSS ---
def apply_theme(theme):
    if theme == "dark":
        st.markdown("""
            <style>
                body, .stApp { background-color: #1e1e1e; color: #ffffff; }
                .css-18e3th9, .css-1d391kg { background-color: #262730; }
                h1, h2, h3, h4, h5, h6, p, li, ul { color: #ffffff !important; }
            </style>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                body, .stApp { background-color: #ffffff; color: #000000; }
                h1, h2, h3, h4, h5, h6, p, li, ul { color: #000000 !important; }
            </style>
            """, unsafe_allow_html=True)

apply_theme(st.session_state["theme"])

# --- Gemini API Key (Do Not Edit This Block) ---
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error(f"Gemini API Key error: {e}")
    model = None

# --- Lottie Animation Loader ---
def load_lottie_url(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None
    return None

# --- Lottie Animations ---
lottie_hero = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_touohxv0.json")  # Rocket launch
lottie_about = load_lottie_url("https://lottie.host/3cc0d79c-4c72-43e9-b705-5c36d6a2067e/N0zPvo2fAx.json")
lottie_projects = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_t0U27CsQcj.json")  # Projects
lottie_chatbot = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_0yfsb3a1.json")  # Chatbot
lottie_footer = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_3rwasyjy.json")   # Thank you

# --- Hero Section ---
with st.container():
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown("""
        <h1 style='font-size: 50px;'>Hey, I'm <span style='color:#FF4B4B;'>Sahil Desai</span> 👋</h1>
        <h3 style='margin-top:-15px;'>2nd Year BTech EXTC | VJTI Mumbai</h3>
        <p style='font-size:18px;'>🚀 Exploring Embedded Systems, Data Science, and AI.</p>
        """, unsafe_allow_html=True)
    with col2:
        if lottie_about:
            st_lottie(lottie_about, height=280, key="hero")

# --- About Me ---
with st.container():
    st.write("---")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <h2>🧠 About Me</h2>
        <p style='font-size:17px;'>I'm a tech enthusiast passionate about building real-world solutions with Embedded Systems and Python.</p>
        <p style='font-size:17px;'>From robotics to OpenCV to data visualizations on the web, I love to blend creativity and code.</p>
        <p style='font-size:17px;'>Currently learning DSA and Data Science to prepare for software internships.</p>
        """, unsafe_allow_html=True)
    with col2:
        if lottie_hero:
            st_lottie(lottie_hero, height=280, key="about")

# --- Projects Section ---
with st.container():
    st.write("---")
    st.markdown("<h2>🛠️ Projects</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("""
        <ul style='font-size:17px;'>
        <li>🤖 <b>Self-balancing Robot</b> using ESP32 and MPU6050</li>
        <li>🚗 <b>Wi-Fi Controlled Car</b> with ESP32 and live camera</li>
        <li>📊 <b>Smart Distance Monitoring</b> system with OLED + Chart.js</li>
        <li>✋ <b>Handwriting Recognition for Kids</b> using OpenCV + Voice</li>
        </ul>
        """, unsafe_allow_html=True)
    with col2:
        if lottie_footer:
            st_lottie(lottie_footer, height=300, key="projects")

# --- Gemini Chatbot Section ---
with st.container():
    st.write("---")
    st.markdown("<h2>💬 Ask Me Anything (Chatbot)</h2>", unsafe_allow_html=True)
    st.caption("Ask about Sahil’s background, achievements, and journey.")
    col1, col2 = st.columns([1, 1])
    with col1:
        user_input = st.text_input("Type your question here:")
        if user_input and model:
            with st.spinner("Thinking..."):
                prompt = f"""
You are an AI assistant for Sahil Desai's portfolio. Only reveal personal background info if asked directly.

PRIVATE INFO (DO NOT reveal unless specifically asked):
- Was a JEE dropper in 2023
- Scored ~98 percentile in JEE Mains (2023, 2024), not qualified JEE Advanced
- Got 99.09 percentile in MHT-CET
- Admitted to VJTI via Defense Quota in 2024
- 8.22 CGPA in first year
- Allotted D-Block hostel on merit
- Had a girlfriend in 12th (keep name private)

User asked: {user_input}
"""
                try:
                    response = model.generate_content(prompt)
                    st.success(response.text)
                except Exception as e:
                    st.error(f"❌ AI response failed: {e}")
    with col2:
        if lottie_chatbot:
            st_lottie(lottie_chatbot, height=280, key="chat")

# --- Footer ---
with st.container():
    st.write("---")
    st.markdown("<h2>✨ Thanks for Visiting!</h2>", unsafe_allow_html=True)
    st.write("This portfolio is built with Python, Streamlit, and love for innovation.")
    if lottie_projects:
        st_lottie(lottie_projects, height=200, key="projects")

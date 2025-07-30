import streamlit as st
from streamlit_lottie import st_lottie
import requests
import google.generativeai as genai

# --- Page Config ---
st.set_page_config(page_title="Sahil Desai | Portfolio", layout="wide", page_icon="💼")

# --- Gemini AI Configuration ---
genai.configure(api_key="AIzaSyD_VwuOiXSi3k8ACj7lxvHN2h_wn14Wcg0")
model = genai.GenerativeModel("gemini-1.5-flash")

# --- Load Lottie Animation from URL ---
def load_lottie_url(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None
    return None

# --- Lottie URLs ---
lottie_hero = load_lottie_url("https://lottie.host/4aabcdb6-bb8b-4c10-8983-24e30e8bb2f5/Q6oRbbF7nP.json")
lottie_about = load_lottie_url("https://lottie.host/0523d100-518b-4ff3-935e-f1be8fdf46a1/lAVJmCQlW1.json")
lottie_projects = load_lottie_url("https://lottie.host/6079eea3-b2cb-4ac7-b8e1-41d5d192bd69/7DqEfHXbHF.json")
lottie_chatbot = load_lottie_url("https://lottie.host/b87dbb7f-6659-49e1-84a6-4d2a9cbb9470/tOekMH4Ch9.json")
lottie_footer = load_lottie_url("https://lottie.host/31c293e2-52f5-48c8-bc9c-1bfc8b716190/yiDXHLoWYb.json")

#  --- CSS Styling ---
# with open("style.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Hero Section ---
with st.container():
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("""
        <h1 style='font-size: 50px;'>Hey, I'm <span style='color:#FF4B4B;'>Sahil Desai</span> 👋</h1>
        <h3 style='margin-top:-15px;'>2nd Year BTech EXTC | VJTI Mumbai</h3>
        <p style='font-size:18px;'>🚀 Exploring Embedded Systems, Data Science, and AI.</p>
        """, unsafe_allow_html=True)
    with col2:
        if lottie_hero:
            st_lottie(lottie_hero, height=300, key="hero")

# --- About Me Section ---
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
        if lottie_about:
            st_lottie(lottie_about, height=300, key="about")

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
        if lottie_projects:
            st_lottie(lottie_projects, height=300, key="projects")

# --- Chatbot Section ---
with st.container():
    st.write("---")
    st.markdown("<h2>💬 Ask Me Anything (Chatbot)</h2>", unsafe_allow_html=True)
    st.caption("Ask about Sahil’s background, achievements, and journey.")

    col1, col2 = st.columns([1, 1])
    with col1:
        user_input = st.text_input("Type your question here:")
        if user_input:
            with st.spinner("Thinking..."):
                prompt = f"""
You are an AI assistant for Sahil Desai's portfolio.
Only reveal personal background info **if asked directly**. Here’s the private info (do NOT show unless user asks):
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

# --- Footer Section ---
with st.container():
    st.write("---")
    st.markdown("<h2>✨ Thanks for Visiting!</h2>", unsafe_allow_html=True)
    st.write("This portfolio is built with Python, Streamlit, and love for innovation.")
    if lottie_footer:
        st_lottie(lottie_footer, height=200, key="footer")

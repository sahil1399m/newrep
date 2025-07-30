import streamlit as st
from streamlit_lottie import st_lottie
import requests
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key="AIzaSyD_VwuOiXSi3k8ACj7lxvHN2h_wn14Wcg0")  # Replace with valid Gemini API key
model = genai.GenerativeModel("gemini-1.5-flash")

# Load Lottie animation from a URL
def load_lottie_url(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Verified working Lottie URLs
animations = {
    "coding": "https://assets9.lottiefiles.com/packages/lf20_dcatp5cr.json",
    "chatbot": "https://assets10.lottiefiles.com/packages/lf20_3rwasyjy.json",
    "rocket": "https://assets1.lottiefiles.com/packages/lf20_qp1q7mct.json",
    "upload": "https://assets2.lottiefiles.com/private_files/lf30_m6j5igxb.json",
    "ai": "https://assets2.lottiefiles.com/packages/lf20_jtbfg2nb.json"
}

# Load all animations
lottie_coding = load_lottie_url(animations["coding"])
lottie_chatbot = load_lottie_url(animations["chatbot"])
lottie_rocket = load_lottie_url(animations["rocket"])
lottie_upload = load_lottie_url(animations["upload"])
lottie_ai = load_lottie_url(animations["ai"])

# Page setup
st.set_page_config(page_title="Sahil Desai Portfolio", layout="wide")
st.markdown("<h1 style='text-align: center;'>👨‍💻 Sahil Desai - Tech Explorer</h1>", unsafe_allow_html=True)

# Top Section
col1, col2 = st.columns(2)
with col1:
    st.subheader("Hello 👋")
    st.title("I am Sahil Desai")
    st.write("Second-Year B.Tech (EXTC) @ VJTI, Mumbai")
    st.write("8.22 CGPA | D-Block Hostel | 2024 Defense Quota | JEE/CET Ranker")
with col2:
    st.image("pimage.png", use_container_width=True)

st.divider()

# About Me
st.subheader("🚀 About Me")
about_col1, about_col2 = st.columns([1, 1])
with about_col1:
    about_text = """
    Passionate about building real-world tech projects. Whether it's OpenCV + ESP32, AI tools for kids,
    or smart monitoring systems, I turn ideas into working systems.

    I believe in learning by building and enjoy exploring DSA, Data Science, Embedded Systems, and Visualization.

    I was a JEE dropper in 2023, scored ~98 percentile, and later got 99.09 percentile in CET.
    Now a proud VJTI student, scoring 8.22 CGPA in Year 1.
    """
    st.markdown(f"<div style='text-align: justify'>{about_text}</div>", unsafe_allow_html=True)
with about_col2:
    if lottie_rocket:
        st_lottie(lottie_rocket, height=280, key="rocket")

st.divider()

# Chatbot
st.subheader("🤖 I Am Sahil's AI Chatbot")
chatbot_col1, chatbot_col2 = st.columns([1, 1])
with chatbot_col1:
    user = st.text_input("Ask me anything...")
    if st.button("Submit"):
        prompt = about_text + "\n" + user
        response = model.generate_content(prompt)
        st.success(response.text)
with chatbot_col2:
    if lottie_chatbot:
        st_lottie(lottie_chatbot, height=280, key="chatbot")

st.divider()

# Skills
st.subheader("📈 My Skills")
skill_col1, skill_col2 = st.columns(2)
with skill_col1:
    st.slider("Python", 0, 100, 85)
    st.slider("C/C++", 0, 100, 70)
    st.slider("Data Structures", 0, 100, 75)
    st.slider("Embedded Systems", 0, 100, 80)
with skill_col2:
    if lottie_ai:
        st_lottie(lottie_ai, height=300, key="skills")

st.divider()

# File Upload
st.subheader("📂 Upload a File")
upload_col1, upload_col2 = st.columns([1, 2])
with upload_col1:
    if lottie_upload:
        st_lottie(lottie_upload, height=150, key="upload")
with upload_col2:
    st.file_uploader("Upload your resume, image, or project files here")

st.divider()
st.caption("Made with ❤️ using Streamlit + Gemini | © Sahil Desai")

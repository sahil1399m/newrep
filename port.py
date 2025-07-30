import streamlit as st
from streamlit_lottie import st_lottie
import requests
import google.generativeai as genai

# Configure Google Gemini API
genai.configure(api_key="YOUR_API_KEY_HERE")  # Replace with your actual API key
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to load lottie animation from URL
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
coding_url = "https://assets10.lottiefiles.com/packages/lf20_jtbfg2nb.json"
chatbot_url = "https://assets2.lottiefiles.com/packages/lf20_sSF6EG.json"
rocket_url = "https://assets2.lottiefiles.com/private_files/lf30_tgb3estd.json"
upload_url = "https://assets3.lottiefiles.com/packages/lf20_q5pk6p1k.json"
ai_brain_url = "https://assets4.lottiefiles.com/packages/lf20_49rdyysj.json"

lottie_coding = load_lottie_url(coding_url)
lottie_chatbot = load_lottie_url(chatbot_url)
lottie_rocket = load_lottie_url(rocket_url)
lottie_upload = load_lottie_url(upload_url)
lottie_ai = load_lottie_url(ai_brain_url)

# Layout
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
    st.image("pimage.png", use_column_width=True)

st.divider()

# About Me Section
st.subheader("🚀 About Me")
about_col1, about_col2 = st.columns([1, 1])
with about_col1:
    persona = """
    Passionate about building innovative real-world tech projects, I thrive at the intersection of software,
    hardware, and creativity. Whether it’s integrating OpenCV with ESP32, crafting kid-friendly AI tools,
    or developing smart monitoring systems, I enjoy turning ideas into working prototypes.

    I believe in learning by building—and I never shy away from experimenting with new tools,
    whether it's LVGL for UI, Chart.js for visualization, or Python for automation. I’m currently
    sharpening my skills in Data Science, DSA, and Embedded Systems to gear up for a software internship in my third year.

    Backstory: I was a JEE dropper in 2023, gave JEE Mains twice (2023 & 2024) scoring ~98 percentile,
    but missed JEE Advanced. Then I aced MHT-CET with 99.09 percentile and got VJTI through Defense quota.
    Scored 8.22 CGPA in 1st year and got hostel (D-Block) on merit.

    Known for staying calm under pressure, I enjoy collaborative work, tight deadlines,
    and finding smart solutions on the fly.
    """
    st.markdown(f"<div style='text-align: justify'>{persona}</div>", unsafe_allow_html=True)
with about_col2:
    st_lottie(lottie_rocket, height=300, key="rocket")

st.divider()

# AI Chatbot Section
st.subheader("🤖 I Am Sahil's AI Chatbot")
chatbot_col1, chatbot_col2 = st.columns([1, 1])
with chatbot_col1:
    user = st.text_input("Ask me anything...")
    if st.button("Submit"):
        prompt = persona + "\n" + user
        response = model.generate_content(prompt)
        st.success(response.text)
with chatbot_col2:
    st_lottie(lottie_chatbot, height=280, key="chatbot")

st.divider()

# Skills Section
st.subheader("📈 My Skills")
skill_col1, skill_col2 = st.columns(2)
with skill_col1:
    st.slider("Python", 0, 100, 85)
    st.slider("C/C++", 0, 100, 70)
    st.slider("Data Structures", 0, 100, 75)
    st.slider("Embedded Systems", 0, 100, 80)
with skill_col2:
    st_lottie(lottie_ai, height=300, key="ai-skills")

st.divider()

# File Upload Section
st.subheader("📂 Upload a File")
upload_col1, upload_col2 = st.columns([1, 2])
with upload_col1:
    st_lottie(lottie_upload, height=150, key="upload")
with upload_col2:
    st.file_uploader("Upload your resume, image, or project files here")

st.divider()
st.caption("Crafted with ❤️ using Streamlit and Gemini API | © Sahil Desai")

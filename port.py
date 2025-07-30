import streamlit as st
from streamlit_lottie import st_lottie
import requests
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key="AIzaSyD_VwuOiXSi3k8ACj7lxvHN2h_wn14Wcg0")
model = genai.GenerativeModel('gemini-1.5-flash')

# Load Lottie animations
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

hello_anim = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_zrqthn6o.json")
chatbot_anim = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_u25cckyh.json")
skills_anim = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_myejiggj.json")

# Header Section
col1, col2 = st.columns(2)
with col1:
    st.subheader("Hello 👋")
    st.title("I am Sahil Desai")
    st.markdown("#### Second-Year B.Tech EXTC Student | VJTI Mumbai")
    st.write("A Tech Explorer and Project Enthusiast.")
with col2:
    st.image("pimage.png", width=250)

st_lottie(hello_anim, height=180)
st.markdown("---")

# Bio / Persona
persona = """
Sahil Desai – Tech Explorer & Project Enthusiast  
Second-Year B.Tech Student | EXTC Branch | VJTI, Mumbai

Passionate about building innovative real-world tech projects, I thrive at the intersection of software, 
hardware, and creativity. Whether it’s integrating OpenCV with ESP32, crafting kid-friendly AI tools, 
or developing smart monitoring systems, I enjoy turning ideas into working prototypes.

I believe in learning by building—and I never shy away from experimenting with new tools, 
whether it's LVGL for UI, Chart.js for visualization, or Python for automation. I’m currently 
sharpening my skills in Data Science, DSA, and Embedded Systems to gear up for a software internship in my third year.

Known for staying calm under pressure, I enjoy collaborative work, tight deadlines, 
and finding smart solutions on the fly. Be it a lab project or a self-initiated build, I bring 
focus, energy, and adaptability to everything I do.
"""

# Chatbot Section
st.markdown("## 🤖 I AM SAHIL's AI CHAT BOT")
st_lottie(chatbot_anim, height=150)
st.write("Ask anything about me:")

user = st.text_input("Type your question here")
if st.button("Submit"):
    prompt = persona + "\n\n" + user
    response = model.generate_content(prompt)
    st.success(response.text)

st.markdown("---")

# Skills Section
st.markdown("## 🧠 My Skills")
st_lottie(skills_anim, height=160)

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Python**")
    st.progress(80)
    st.markdown("**Data Science**")
    st.progress(70)
with col2:
    st.markdown("**DSA**")
    st.progress(75)
    st.markdown("**Embedded Systems**")
    st.progress(65)

st.markdown("---")

# File Uploader
st.markdown("## 📤 Upload Your File")
st.file_uploader("Choose a file (pdf, image, docx)", type=["pdf", "jpg", "png", "docx"])

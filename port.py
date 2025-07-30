import streamlit as st
from streamlit_lottie import st_lottie
import requests
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="Sahil's Portfolio", page_icon="🧑‍💻", layout="wide")

# Google Gemini API Key
genai.configure(api_key="AIzaSyD_VwuOiXSi3k8ACj7lxvHN2h_wn14Wcg0")
model = genai.GenerativeModel("gemini-pro")

# Function to load Lottie animations
def load_lottie_url(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None

# Load Animations
lottie_coding = load_lottie_url("https://lottie.host/4aabcdb6-bb8b-4c10-8983-24e30e8bb2f5/Q6oRbbF7nP.json")
lottie_rocket = load_lottie_url("https://lottie.host/1ab9603f-4b3d-481e-bfa9-12fdc6a32d4b/5kVrZ0UBVm.json")
lottie_chat = load_lottie_url("https://lottie.host/b87dbb7f-6659-49e1-84a6-4d2a9cbb9470/tOekMH4Ch9.json")

# Header
with st.container():
    st.title("Hey, I'm Sahil 👋")
    st.subheader("BTech EXTC Student at VJTI | Passionate about AI, Robotics & Software")
    st.write("Welcome to my interactive portfolio built with Streamlit!")

# About Section
with st.container():
    st.write("---")
    left_col, right_col = st.columns(2)
    with left_col:
        st.header("About Me")
        st.write("""
        I am an enthusiastic second-year Electronics and Telecommunication Engineering student at VJTI, Mumbai.
        I love building tech projects with ESP32, OpenCV, and Data Science. I'm aiming for a software internship in my third year.
        """)
    with right_col:
        st_lottie(lottie_coding, height=300, key="coding")

# Projects
with st.container():
    st.write("---")
    st.header("Projects 💡")
    st.write("### Here are a few things I've worked on:")
    st.markdown("- 🤖 **Self-balancing robot** with ESP32 + LVGL")
    st.markdown("- 🚗 **WiFi-controlled smart car** with live video & servo")
    st.markdown("- 📈 **Smart distance monitor** with web graph (Chart.js)")
    st.markdown("- ✋ **OpenCV Kids App** — draws letters via hand & speaks using TTS")

# AI Chatbot Section
with st.container():
    st.write("---")
    st.header("💬 Ask Me Anything (Chatbot)")
    st.write("You can ask me questions about my journey, background, or projects.")
    st_lottie(lottie_chat, height=250, key="chat")

    user_input = st.text_input("Ask a question:")
    if user_input:
        with st.spinner("Thinking..."):
            prompt = f"""
You are an AI assistant for Sahil Desai's portfolio. Only reveal personal info when asked.
Here’s private info you can use ONLY IF ASKED:
- JEE dropper in 2023
- ~98 percentile in JEE Mains (2023 & 2024), but did not qualify JEE Advanced
- 99.09 percentile in MHT-CET PCM
- Joined VJTI in 2024 via Defense Quota
- CGPA: 8.22 in 1st year
- Got hostel D-block seat on merit
- Had a girlfriend in 12th (keep her name private)

User asks: {user_input}
"""
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
            except Exception as e:
                st.error("❌ AI failed to respond. Please try again.")

# Footer
with st.container():
    st.write("---")
    st.header("🚀 Let's Connect")
    st.write("Find me on:")
    st.markdown("""
- [LinkedIn](https://www.linkedin.com/in/YOUR_USERNAME)
- [GitHub](https://github.com/YOUR_USERNAME)
- [Email](mailto:your_email@example.com)
""")
    st_lottie(lottie_rocket, height=250, key="rocket")


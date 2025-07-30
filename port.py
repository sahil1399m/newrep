import streamlit as st
from streamlit_lottie import st_lottie
import requests
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Sahil Desai | Portfolio", layout="wide", page_icon="💼")

# --- Gemini AI Config ---
genai.configure(api_key="AIzaSyD_VwuOiXSi3k8ACj7lxvHN2h_wn14Wcg0")
model = genai.GenerativeModel("gemini-pro")

# --- Load Lottie Animation ---
def load_lottie_url(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None
    return None

# --- Lottie Animations (safe links) ---
lottie_hero = load_lottie_url("https://lottie.host/4aabcdb6-bb8b-4c10-8983-24e30e8bb2f5/Q6oRbbF7nP.json")
lottie_about = load_lottie_url("https://lottie.host/0523d100-518b-4ff3-935e-f1be8fdf46a1/lAVJmCQlW1.json")
lottie_projects = load_lottie_url("https://lottie.host/6079eea3-b2cb-4ac7-b8e1-41d5d192bd69/7DqEfHXbHF.json")
lottie_chatbot = load_lottie_url("https://lottie.host/b87dbb7f-6659-49e1-84a6-4d2a9cbb9470/tOekMH4Ch9.json")
lottie_footer = load_lottie_url("https://lottie.host/31c293e2-52f5-48c8-bc9c-1bfc8b716190/yiDXHLoWYb.json")

# --- Header / Hero Section ---
with st.container():
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.title("Hey, I'm Sahil Desai 👋")
        st.subheader("2nd Year BTech EXTC | VJTI Mumbai")
        st.write("🚀 Building cool projects with ESP32, OpenCV, Data Science, and AI.")
    with col2:
        if lottie_hero:
            st_lottie(lottie_hero, height=300, key="hero")

# --- About Section ---
with st.container():
    st.write("---")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.header("🧠 About Me")
        st.write("""
        I’m a passionate tech explorer from VJTI who loves building real-world systems.
        I’ve worked with ESP32s, created smart AI tools for kids, and made live data monitoring systems using Python + JS.

        Currently, I’m improving my DSA, Embedded, and Data Science skills aiming for a software internship in my 3rd year.
        """)
    with col2:
        if lottie_about:
            st_lottie(lottie_about, height=300, key="about")

# --- Projects Section ---
with st.container():
    st.write("---")
    st.header("🛠️ Projects")
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("- 🤖 **Self-balancing robot** with ESP32 + LVGL UI")
        st.markdown("- 🚗 **Wi-Fi Controlled Car** with live-streaming & servo")
        st.markdown("- 📊 **Smart Distance Monitor**: ESP32 + OLED + Chart.js")
        st.markdown("- ✋ **OpenCV Learning Tool**: Kids draw letters with hand, get voice feedback")
    with col2:
        if lottie_projects:
            st_lottie(lottie_projects, height=300, key="projects")

# --- Chatbot Section ---
with st.container():
    st.write("---")
    st.header("💬 Ask Me Anything (Chatbot)")
    st.caption("Ask about Sahil’s background, journey, or achievements.")

    col1, col2 = st.columns([1, 1])
    with col1:
        user_input = st.text_input("Type your question here:")
        if user_input:
            with st.spinner("Thinking..."):
                prompt = f"""
You are a portfolio AI assistant for Sahil Desai. If the user asks personal things, reveal only this:
- Was a JEE dropper (2023)
- 98 percentile JEE Mains (2023 & 2024), not qualified JEE Adv
- 99.09 percentile in CET (PCM)
- Joined VJTI via Defense Quota in 2024
- 8.22 CGPA in first year
- D-Block Hostel on merit
- Had a girlfriend in 12th (name private)

User asked: {user_input}
"""
                try:
                    response = model.generate_content(prompt)
                    st.success(response.text)
                except Exception as e:
                    st.error("❌ AI failed. Please try again.")
    with col2:
        if lottie_chatbot:
            st_lottie(lottie_chatbot, height=280, key="chat")

# --- Resume Upload / Download ---
with st.container():
    st.write("---")
    st.header("📄 Resume & Files")
    col1, col2 = st.columns([1, 1])
    with col1:
        uploaded = st.file_uploader("Upload your resume or project file")
    with col2:
        with open("Sahil_Resume.pdf", "rb") as file:
            st.download_button("📥 Download My Resume", file, file_name="Sahil_Desai_Resume.pdf")

# --- Footer ---
with st.container():
    st.write("---")
    st.header("🌐 Connect With Me")
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("""
- 🔗 [LinkedIn](https://www.linkedin.com/in/YOUR_USERNAME)
- 💻 [GitHub](https://github.com/YOUR_USERNAME)
- 📧 [Email](mailto:your_email@example.com)
""")
    with col2:
        if lottie_footer:
            st_lottie(lottie_footer, height=250, key="footer")

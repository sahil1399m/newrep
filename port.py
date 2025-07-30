import streamlit as st
from streamlit_lottie import st_lottie
import google.generativeai as genai
import requests

# Configure Google Gemini
genai.configure(api_key="YOUR_API_KEY_HERE")  # Replace with your real key
model = genai.GenerativeModel('gemini-1.5-flash')

# Load Lottie Animation
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "https://lottie.host/5f15b6c0-9f3e-4b16-8c59-f8b4d4a11ff5/YgK4d7zHGS.json"
lottie_coding = load_lottie_url(lottie_url)

# Set page config
st.set_page_config(page_title="Sahil's Portfolio", page_icon="💡", layout="wide")

# Hero Section
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Hi there! 👋")
        st.title("I'm Sahil Desai")
        st.write("Tech explorer, builder, and a second-year EXTC student at VJTI Mumbai.")
    with col2:
        st.image("pimage.png", width=300)

# Lottie animation
with st.container():
    if lottie_coding:
        st_lottie(lottie_coding, height=300, key="coding")
    else:
        st.warning("⚠️ Animation failed to load.")

# Persona Description
persona = """
I’m Sahil Desai – a tech explorer and hands-on builder, currently in my second year of B.Tech (EXTC) at VJTI, Mumbai.

🔧 I love turning creative tech ideas into real-world projects—from OpenCV + ESP32 setups to interactive AI tools for kids, smart monitoring systems, and much more.

📚 I'm sharpening my skills in Data Science, Embedded Systems, and DSA, gearing up for a software internship in my third year.

🛠️ I'm always experimenting—LVGL for UI, Python for automation, Chart.js for visualization, you name it.

💡 I believe in learning by building and staying calm under pressure. Whether it’s a lab assignment or self-driven innovation, I bring energy, clarity, and adaptability to every task.

🎓 Backstory:
- Dropped for JEE in 2023.
- Appeared for JEE Mains in 2023 & 2024 (Scored ~98 percentile).
- Didn't qualify for JEE Advanced.
- Scored 99.09 percentile in MHT-CET (PCM).
- Got admission in VJTI via Defense quota (2024).
- CGPA: 8.22 in First Year.
- Allotted hostel in D-Block on merit.
- Had a girlfriend in 12th (Name private 😉).
"""

# AI Chatbot Section
st.divider()
st.title("🤖 Ask Sahil's AI Chatbot")
st.markdown("Ask anything about my journey, skills, or background.")

user = st.text_input("Type your question here:")

if st.button("Submit", use_container_width=True):
    prompt = persona + "\nUser Question: " + user
    response = model.generate_content(prompt)
    st.write(response.text)

# Skills Section
st.divider()
st.title("💼 My Skills")
st.slider("Python", 0, 100, 85)
st.slider("Embedded Systems", 0, 100, 75)
st.slider("Data Science", 0, 100, 65)
st.slider("OpenCV & Computer Vision", 0, 100, 80)

# Upload Section
st.divider()
st.title("📁 File Uploader")
st.file_uploader("Upload your resume, project files, etc.")

# Footer
st.divider()
st.caption("Built with ❤️ using Streamlit | © Sahil Desai 2025")

import streamlit as st
from streamlit_lottie import st_lottie
import requests
import google.generativeai as genai

# Configure API
genai.configure(api_key="AIzaSyD_VwuOiXSi3k8ACj7lxvHN2h_wn14Wcg0")
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to load Lottie animation from URL
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load a cool Lottie animation
lottie_coding = load_lottie_url("https://lottie.host/1c6e71c8-bb42-443e-a387-0523a91f933b/YRTv3RWGlj.json")

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("Navigation")
st.sidebar.markdown("👋 Hello, I'm Sahil Desai")
st.sidebar.image("pimage.png", width=200)
st.sidebar.markdown("---")

# ---------------------------
# Home
# ---------------------------
st.title("🚀 Welcome to Sahil's Portfolio")

col1, col2 = st.columns(2)
with col1:
    st.header("Hey, I'm Sahil Desai 👋")
    st.write("""
    - 🎓 Second-Year B.Tech (EXTC) @ VJTI, Mumbai  
    - 🔬 Tech Explorer | Hardware-Software Enthusiast  
    - 🎯 Scored 99.09 percentile in MHT-CET (Defense Quota)  
    - 🧠 8.22 CGPA | D-Block Hostel (Merit-Based)
    """)
with col2:
    st_lottie(lottie_coding, height=300, key="coding")

# ---------------------------
# Persona / About Me
# ---------------------------
with st.expander("💡 About Me"):
    persona = """
    I'm a passionate techie who enjoys blending hardware and software into real-world systems.  
    Whether it's OpenCV + ESP32, Data Visualization, or building AI tools for kids — I just love creating.  
    I believe in "learning by building" and am currently sharpening my skills in Data Science, DSA, and Embedded Systems.

    ▶ I gave JEE Mains twice (~98 percentile), missed Advanced but bounced back with 99.09% in MHT-CET.  
    ▶ Got into VJTI through Defense quota (2024), earned 8.22 CGPA in 1st year & was allotted D-Block hostel.

    ✨ Calm, collaborative, creative — and always curious to try something new!
    """
    st.markdown(persona)

# ---------------------------
# ChatBot
# ---------------------------
st.subheader("🤖 Ask Me Anything")
user_input = st.text_input("Type your question about me...")
if st.button("Submit"):
    prompt = persona + user_input
    response = model.generate_content(prompt)
    st.success(response.text)

# ---------------------------
# Skills
# ---------------------------
st.subheader("🧰 My Skills")
st.slider("Python", 0, 100, 80)
st.slider("Embedded Systems", 0, 100, 70)
st.slider("OpenCV", 0, 100, 65)
st.slider("Data Science", 0, 100, 60)
st.slider("DSA", 0, 100, 70)

# ---------------------------
# File Upload
# ---------------------------
st.subheader("📁 Upload Your File")
st.file_uploader("Choose a file")

# ---------------------------
# Contact
# ---------------------------
st.markdown("---")
st.subheader("📬 Contact Me")
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    if st.form_submit_button("Send"):
        st.success("Thanks! Your message has been sent.")

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.markdown("Made with ❤️ by Sahil Desai | [LinkedIn](https://linkedin.com) | [GitHub](https://github.com)")

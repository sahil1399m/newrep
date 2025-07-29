import streamlit as st
import google.generativeai as genai

# Use this for local testing (unsafe for production):
# genai.configure(api_key="your-api-key-here")

# ✅ Use secret in production
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Load model
model = genai.GenerativeModel('gemini-1.5-flash')

# UI layout
col1, col2 = st.columns(2)
with col1:
    st.subheader("Hello :wave:")
    st.title("Hello, I am Sahil Desai")
with col2:
    st.image("pimage.png")

st.title("I AM SAHIL's AI CHAT BOT")
st.write("Ask anything about me 👇")

# Persona block
persona = """
Sahil Desai – Tech Explorer & Project Enthusiast

Second-Year B.Tech Student | EXTC Branch | VJTI, Mumbai

Passionate about building real-world tech projects at the intersection of software and hardware.
Enjoys working with OpenCV, ESP32, LVGL, Python, and Data Science tools.
Calm under pressure, team-friendly, and quick problem-solver.
"""

# User input
user = st.text_input("Type your question here:")

# Submit button
if st.button("SUBMIT", use_container_width=True):
    if user.strip() == "":
        st.warning("❗ Please enter a question before submitting.")
    else:
        full_prompt = persona + "\n\nQuestion: " + user
        try:
            response = model.generate_content(full_prompt)
            st.markdown("**Response:**")
            st.write(response.text)
        except Exception as e:
            st.error(f"❌ Error from Gemini: {str(e)}")

# Skills slider
st.title("My Skills")
st.slider("Python", 0, 100, 80)

# File upload
st.file_uploader("Upload your file here")

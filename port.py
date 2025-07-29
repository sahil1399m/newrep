import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyD_VwuOiXSi3k8ACj7lxvHN2h_wn14Wcg0")
model = genai.GenerativeModel('gemini-1.5-flash')

# --- Custom CSS for better visuals ---
st.markdown("""
    <style>
        body {
            background-color: #f4f6f8;
        }
        .title {
            color: #2c3e50;
            font-size: 40px;
            font-weight: bold;
        }
        .subtitle {
            color: #7f8c8d;
            font-size: 22px;
            margin-bottom: 20px;
        }
        .persona-box {
            background-color: #ecf0f1;
            padding: 20px;
            border-radius: 12px;
            margin-top: 20px;
            font-size: 18px;
            color: #2c3e50;
        }
        .chat-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 12px;
            margin-top: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .slider-label {
            font-size: 18px;
            font-weight: 600;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Layout with columns ---
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="title">Hello 👋</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">I am Sahil Desai</div>', unsafe_allow_html=True)

with col2:
    st.image("pimage.png", width=250)

# --- Persona Section ---
st.markdown('<div class="chat-box"><h3>I AM SAHIL\'s AI CHAT BOT</h3><p>Ask anything about me 👇</p></div>', unsafe_allow_html=True)

# --- Chat Input ---
user = st.text_input("Type your question here:")
if st.button("Submit", use_container_width=True):
    prompt = f"{persona}\n\n{user}"
    response = model.generate_content(prompt)
    st.markdown(f'<div class="chat-box"><b>Answer:</b><br>{response.text}</div>', unsafe_allow_html=True)

# --- Persona Bio Section ---
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

st.markdown(f'<div class="persona-box">{persona}</div>', unsafe_allow_html=True)

# --- Skills Slider ---
st.markdown('<div class="slider-label">My Skills</div>', unsafe_allow_html=True)
python_level = st.slider("Python", 0, 100, 80)
ds_level = st.slider("Data Science", 0, 100, 70)
dsa_level = st.slider("DSA", 0, 100, 75)
embedded_level = st.slider("Embedded Systems", 0, 100, 65)

# --- File Upload ---
st.markdown('<div class="slider-label">Upload Your File</div>', unsafe_allow_html=True)
st.file_uploader("Choose a file", type=["pdf", "docx", "txt", "jpg", "png"])

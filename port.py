import  streamlit as st
import google.generativeai as genai
api_key=st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model=genai.GenerativeModel('gemini-1.5-flash')
col1,col2=st.columns(2)
with col1:
    st.subheader("Hello :wave:")
    st.title("Hello , "
        "I am Sahil Desai ")
with col2:
    st.image("pimage.png")

st.title("  ")
persona = """Sahil Desai – Tech Explorer & Project Enthusiast Second-Year B.Tech Student | EXTC Branch | VJTI, Mumbai

 Passionate about building innovative real-world tech projects, I thrive at the intersection of software, 
hardware, and creativity. Whether it’s integrating OpenCV with ESP32, crafting kid-friendly AI tools, 
or developing smart monitoring systems, I enjoy turning ideas into working prototypes.

 I believe in learning by building—and I never shy away from experimenting with new tools, 
whether it's LVGL for UI, Chart.js for visualization, or Python for automation. I’m currently 
sharpening my skills in Data Science, DSA, and Embedded Systems to gear up for a software internship in my third year.

 Known for staying calm under pressure, I enjoy collaborative work, tight deadlines, 
and finding smart solutions on the fly. Be it a lab project or a self-initiated build, I bring 
focus, energy, and adaptability to everything I do."""
st.title("I AM SAHIL's AI CHAT BOT")
st.write("Ask anything about me")
user=st.text_input("type here")
if st.button("SUMBIT", use_container_width=400):
    prompt=persona+user
    response=model.generate_content(prompt)
    st.write(response.text)
st.write(" ")
st.title("My Skills")
st.slider("python",0,100,80)
st.write(" ")
st.file_uploader("upload your file here")


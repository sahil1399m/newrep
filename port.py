import streamlit as st

# Page config
st.set_page_config(page_title="Sahil Desai | Portfolio", layout="wide")

# Custom CSS for animations and layout
st.markdown("""
    <style>
    body {
        font-family: 'Segoe UI', sans-serif;
    }

    .title {
        font-size: 60px;
        font-weight: bold;
        background: linear-gradient(to right, #00c6ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: fadeIn 2s ease-in-out;
    }

    .subtitle {
        font-size: 30px;
        color: #666;
        margin-bottom: 20px;
        animation: slideUp 1.5s ease-out;
    }

    .card {
        background-color: #ffffff10;
        padding: 1.5rem;
        border-radius: 20px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 20px;
        animation: fadeInUp 1s ease-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes slideUp {
        from { transform: translateY(30px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }

    @keyframes fadeInUp {
        0% { transform: translateY(20px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }

    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown('<div class="title">Sahil Desai</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Engineer | Innovator | Learner</div>', unsafe_allow_html=True)

# About section
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("About Me")
    st.write("""
    I'm Sahil Desai, a passionate engineering student at VJTI. I enjoy building real-world tech projects that combine software, hardware, and AI. Currently exploring OpenCV, IoT with ESP32, and data science.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Projects section
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Projects")
    st.markdown("""
    - 🚘 **Driver Drowsiness Detection** using OpenCV & alert system with ESP32  
    - 📊 **Smart Distance Monitoring** with live web interface and servo control  
    - 🧒 **Kids Learn with AI** – finger-writing + voice assistant using OpenCV  
    - 🎯 **Face-based Proxy Detection** for attendance management
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Skills section
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Skills")
    st.markdown("""
    - 👨‍💻 Python, C++, HTML/CSS  
    - 🤖 OpenCV, Streamlit, TensorFlow  
    - 🌐 ESP32, IoT, Microcontrollers  
    - 📈 Data Science (pandas, matplotlib, scikit-learn)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Contact section
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Contact")
    st.markdown("""
    - 📧 sahildesai@example.com  
    - 🔗 [LinkedIn](https://www.linkedin.com)  
    - 💻 [GitHub](https://github.com)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

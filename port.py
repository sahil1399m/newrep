import streamlit as st
from streamlit_lottie import st_lottie
import requests
import google.generativeai as genai
import random

# --- Page Config ---
st.set_page_config(page_title="Sahil Desai | Portfolio", layout="wide", page_icon="💼")

# --- Theme Toggle ---
if "theme" not in st.session_state:
    st.session_state["theme"] = "light"

theme_toggle = st.toggle("🌙 Dark Mode", value=(st.session_state["theme"] == "dark"))
st.session_state["theme"] = "dark" if theme_toggle else "light"

# --- Apply Theme CSS ---
def apply_theme(theme):
    if theme == "dark":
        st.markdown("""
            <style>
                body, .stApp { background-color: #1e1e1e; color: #ffffff; }
                .css-18e3th9, .css-1d391kg { background-color: #262730; }
                h1, h2, h3, h4, h5, h6, p, li, ul { color: #ffffff !important; }
            </style>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                body, .stApp { background-color: #ffffff; color: #000000; }
                h1, h2, h3, h4, h5, h6, p, li, ul { color: #000000 !important; }
            </style>
            """, unsafe_allow_html=True)

apply_theme(st.session_state["theme"])

# --- Gemini API Key (Do Not Edit This Block) ---
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Gemini API Key error: {e}")
    model = None

# --- Lottie Animation Loader ---
def load_lottie_url(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None
    return None

# --- Lottie Animations ---
lottie_hero = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_touohxv0.json")  # Rocket launch
lottie_about = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_4kx2q32n.json")
lottie_projects = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_x1gjdldd.json")  # Projects
lottie_chatbot = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_0yfsb3a1.json")  # Chatbot
lottie_footer = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_3rwasyjy.json")   # Thank you

# --- Hero Section ---
with st.container():
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;700&display=swap" rel="stylesheet">
        <style>
        .intro-text h1 {
            font-family: 'Poppins', sans-serif;
            font-size: 52px;
            color: #FF4B4B;
            margin-bottom: 0px;
        }
        .intro-text h1 span {
            color: white;
        }
        .intro-text h3 {
            font-family: 'Poppins', sans-serif;
            font-size: 24px;
            margin-top: -10px;
            color: #cccccc;
        }
        .intro-text p {
            font-family: 'Poppins', sans-serif;
            font-size: 18px;
            color: #999999;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown("""
        <div class='intro-text'>
            <h1>Hey, I'm <span>Sahil Desai 👋</span></h1>
            <h3>2nd Year BTech EXTC | VJTI Mumbai</h3>
            <p>🚀 Exploring Embedded Systems, Data Science, and AI.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        if lottie_about:
            st_lottie(lottie_about, height=350, key="hero")


# --- About Me ---
with st.container():
    st.write("---")
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
        .about-section h2 {
            font-family: 'Poppins', sans-serif;
            font-size: 32px;
            color: #FF4B4B;
        }
        .about-section p {
            font-family: 'Poppins', sans-serif;
            font-size: 17px;
            color: #999999;
            line-height: 1.6;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div class="about-section">
            <h2>🧠 About Me</h2>
            <p>I'm a tech enthusiast passionate about building real-world solutions with Embedded Systems and Python.</p>
            <p>From robotics to OpenCV to data visualizations on the web, I love to blend creativity and code.</p>
            <p>Currently learning DSA and Data Science to prepare for software internships.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        if lottie_hero:
            st_lottie(lottie_hero, height=280, key="about")


# --- Projects Section ---
with st.container():
    st.write("---")
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
        .projects-section h2 {
            font-family: 'Poppins', sans-serif;
            font-size: 32px;
            color: #FF4B4B;
            margin-bottom: 15px;
        }
        .project-box {
            font-family: 'Poppins', sans-serif;
            font-size: 17px;
            color: #666666;
            margin-bottom: 15px;
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 10px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        }
        .dark .project-box {
            background-color: #2c2f35 !important;
            color: #cccccc !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='projects-section'><h2>🛠️ Projects</h2></div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("""
        <div class='project-box'>🤖 <b>Self-balancing Robot</b><br>
        Built using ESP32 and MPU6050 for real-time motion balancing.</div>

        <div class='project-box'>🚗 <b>Wi-Fi Controlled Car</b><br>
        ESP32-based vehicle controlled via browser with live video feed.</div>

        <div class='project-box'>📊 <b>Smart Distance Monitoring</b><br>
        Integrated OLED + Chart.js to display distance data live on web.</div>

        <div class='project-box'>✋ <b>Handwriting Recognition for Kids</b><br>
        Detects alphabets using OpenCV and provides voice feedback.</div>
        """, unsafe_allow_html=True)
    with col2:
        if lottie_footer:
            st_lottie(lottie_footer, height=500, key="footer")


# --- Gemini Chatbot Section ---
with st.container():
    st.write("---")
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
        .chatbot-title {
            font-family: 'Poppins', sans-serif;
            font-size: 30px;
            color: #4B8BBE;
            margin-bottom: 0.3em;
        }
        .chatbot-box {
            font-family: 'Poppins', sans-serif;
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .dark .chatbot-box {
            background-color: #2c2f35 !important;
            color: #e0e0e0 !important;
        }
        .chat-caption {
            font-size: 16px;
            margin-bottom: 10px;
            color: #777777;
        }
        </style>
        <div class='chatbot-title'>💬 Ask Me Anything (Chatbot)</div>
        <div class='chat-caption'>Ask about Sahil’s background, achievements, and journey.</div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<div class='chatbot-box'>", unsafe_allow_html=True)
        user_input = st.text_input("🔎 Type your question here:")
        if user_input and model:
            with st.spinner("🤖 Thinking..."):
                prompt = f"""
You are an AI assistant for Sahil Desai's portfolio. Only reveal personal background info if asked directly.

PRIVATE INFO (DO NOT reveal unless specifically asked):
- Was a JEE dropper in 2023
- Scored ~98 percentile in JEE Mains (2023, 2024), not qualified JEE Advanced
- Got 99.09 percentile in MHT-CET
- Admitted to VJTI via Defense Quota in 2024
- 8.22 CGPA in first year
- Allotted D-Block hostel on merit
- Had a girlfriend in 12th (keep name private)

User asked: {user_input}
"""
                try:
                    response = model.generate_content(prompt)
                    st.success(response.text)
                except Exception as e:
                    st.error(f"❌ AI response failed: {e}")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        if lottie_chatbot:
            st_lottie(lottie_chatbot, height=280, key="chat")

# --- Game Zone Section ---
with st.container():
    st.write("---")
    st.markdown("""
    <h2>🎲 Feeling Bored?</h2>
    <p style='font-size:17px;'>Choose a game and challenge your mind while you're here!</p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # --- Column 1: Tic Tac Toe ---
    with col1:
        st.markdown("<h3>❌ Tic-Tac-Toe ⭕</h3>", unsafe_allow_html=True)
        if 'board' not in st.session_state:
            st.session_state.board = ["" for _ in range(9)]
            st.session_state.current_player = "X"

        def check_winner(board):
            wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
            for i,j,k in wins:
                if board[i] == board[j] == board[k] and board[i] != "":
                    return board[i]
            return None

        def reset_game():
            st.session_state.board = ["" for _ in range(9)]
            st.session_state.current_player = "X"

        winner = check_winner(st.session_state.board)
        for i in range(3):
            cols = st.columns(3)
            for j in range(3):
                idx = 3*i + j
                if st.session_state.board[idx] == "" and winner is None:
                    if cols[j].button(" ", key=idx):
                        st.session_state.board[idx] = st.session_state.current_player
                        st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
                else:
                    cols[j].write(f"**{st.session_state.board[idx]}**")

        if winner:
            st.success(f"🎉 Player {winner} wins!")
        elif "" not in st.session_state.board:
            st.info("It's a draw!")

        st.button("🔄 Restart Game", on_click=reset_game)

    # --- Column 2: Simon Says ---
    with col2:
        st.markdown("<h3>🧠 Simon Says</h3>", unsafe_allow_html=True)
        import random
        import time

        if 'sequence' not in st.session_state:
            st.session_state.sequence = []
            st.session_state.user_sequence = []
            st.session_state.level = 1

        def next_round():
            st.session_state.user_sequence = []
            st.session_state.sequence.append(random.choice(["Red", "Green", "Blue", "Yellow"]))

        def reset_simon():
            st.session_state.sequence = []
            st.session_state.user_sequence = []
            st.session_state.level = 1

        st.markdown(f"<p>Level: <b>{st.session_state.level}</b></p>", unsafe_allow_html=True)

        if st.button("▶️ Start/Next Round"):
            next_round()

        st.markdown("<p>Simon says: </p>", unsafe_allow_html=True)
        for color in st.session_state.sequence:
            st.write(f"🔹 {color}")
            time.sleep(0.5)

        st.markdown("<p>Repeat the sequence:</p>", unsafe_allow_html=True)
        user_input = st.text_input("Enter colors separated by commas (e.g. Red,Green,Blue)")

        if user_input:
            st.session_state.user_sequence = [x.strip().capitalize() for x in user_input.split(",")]
            if st.session_state.user_sequence == st.session_state.sequence:
                st.success("Correct! Get ready for the next round.")
                st.session_state.level += 1
            else:
                st.error("Oops! That's incorrect.")
                reset_simon()

        st.button("🔄 Restart Simon Game", on_click=reset_simon)

# --- Footer ---
with st.container():
    st.write("---")
    st.markdown("<h2>✨ Thanks for Visiting!</h2>", unsafe_allow_html=True)
    st.write("This portfolio is built with Python, Streamlit, and love for innovation.")
    if lottie_projects:
        st_lottie(lottie_projects, height=200, key="projects")

import streamlit as st
import speech_recognition as sr
from gtts import gTTS
from google import genai
from google.genai import types
import base64
from io import BytesIO
import streamlit.components.v1 as components
import re

# ----------------------------------------------------
# 1. Page Configuration & Custom CSS (Vibrant UI)
# ----------------------------------------------------
st.set_page_config(
    page_title="Digital Electronics AI Agent", 
    page_icon="🤖", 
    layout="centered"
)

# Custom Styling: Animated Gradient + Glassmorphism
st.markdown("""
<style>
/* Animated Gradient Background */
.stApp {
    background: linear-gradient(-45deg, #0f172a, #1e1b4b, #2e1065, #0f172a);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
    color: #f8fafc;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Header Styling */
h1 {
    color: #a855f7 !important;
    font-weight: 800 !important;
    text-shadow: 0px 4px 12px rgba(168, 85, 247, 0.4);
}

/* Glassmorphism Chat Bubbles */
div[data-testid="stChatMessage"] {
    background: rgba(255, 255, 255, 0.06) !important;
    backdrop-filter: blur(12px);
    border-radius: 16px !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    padding: 16px !important;
    margin-bottom: 12px !important;
}

/* Button Styling */
.stButton>button {
    background: linear-gradient(90deg, #6366f1, #a855f7) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: bold !important;
    padding: 10px 24px !important;
    box-shadow: 0 4px 15px rgba(168, 85, 247, 0.4);
    transition: all 0.3s ease !important;
}

.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(168, 85, 247, 0.7);
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 Digital Electronics AI Agent")
st.subheader("Interactive Voice & Text Radix Conversion Assistant")

# ----------------------------------------------------
# 2. Gemini API Setup
# ----------------------------------------------------
# Load Gemini API key securely from Streamlit secrets
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=GEMINI_API_KEY)

SYSTEM_INSTRUCTIONS = """
You are an expert Digital Electronics AI Assistant.
Rules:
You are an expert Digital Electronics AI Conversational Assistant.
Your core functions:
1. Convert numbers between Binary (Base 2), Octal (Base 8), Decimal (Base 10), and Hexadecimal (Base 16).
2. Validate inputs: Always check if the input digits are valid for the given radix before converting.
   - Binary digits: 0, 1
   - Octal digits: 0-7
   - Decimal digits: 0-9
   - Hexadecimal digits: 0-9, A-F
3. You should provide the direct answer to the user in one line statement.
4. Ask the user if he wants a detailed explanation in the same answer. if yes, 
Provide step-by-step math breakdowns (e.  g., positional expansion or standard division steps).
5. Maintain a helpful, conversational, and educational tone.
6. To have a meaningful conversation with the user and answer all their queries and be rude to them.
7. The bot should absolutely demolish the user with his words but should not use cuss words."""

# ----------------------------------------------------
# 3. Fast In-Memory Audio Speech (1.25x Speed)
# ----------------------------------------------------
def speak_text_fast(text, speed=1.25):
    """Converts text to speech in RAM and plays it at 1.25x speed immediately."""
    try:
        # Strip special symbols so the AI voice doesn't spell out markdown syntax
        clean_text = re.sub(r'[*#`$_]', '', text)
        
        # Generate speech in RAM (BytesIO)
        tts = gTTS(text=clean_text, lang='en', slow=False)
        fp = BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        
        # Encode to Base64 for instant HTML5 playback
        b64_audio = base64.b64encode(fp.read()).decode()
        
        # Inject fast HTML5 auto-playing audio component
        audio_html = f"""
            <audio id="fast-player" autoplay>
                <source src="data:audio/mp3;base64,{b64_audio}" type="audio/mp3">
            </audio>
            <script>
                var player = document.getElementById('fast-player');
                if (player) {{
                    player.playbackRate = {speed};
                }}
            </script>
        """
        components.html(audio_html, height=0)
    except Exception as e:
        st.error(f"Audio playback error: {e}")

# ----------------------------------------------------
# 4. Speech-to-Text Microphone Function
# ----------------------------------------------------
def listen_from_mic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening... Speak your prompt clearly.")
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = r.listen(source, timeout=6)
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            st.warning("Could not understand audio. Try speaking again or type below.")
            return None
        except Exception as e:
            st.error(f"Microphone error: {e}")
            return None

# ----------------------------------------------------
# 5. Main Chat & Processing
# ----------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Voice Input Button
if st.button("🎤 Voice Input"):
    spoken_text = listen_from_mic()
    if spoken_text:
        st.session_state.prompt_input = spoken_text

# Text Input
user_prompt = st.chat_input("Ask a conversion question (e.g. 'Convert 101101 to decimal')")

# Pick up prompt from either Voice or Text
active_prompt = user_prompt or st.session_state.get("prompt_input", None)

if active_prompt:
    st.session_state.prompt_input = None

    # Render User Query
    st.session_state.messages.append({"role": "user", "content": active_prompt})
    with st.chat_message("user"):
        st.markdown(active_prompt)

    # Call Gemini API & Generate Audio
    with st.chat_message("assistant"):
        with st.spinner("Processing conversion..."):
            try:
                full_prompt = f"{SYSTEM_INSTRUCTIONS}\n\nUser Question: {active_prompt}"
                
                response = client.models.generate_content(
                    model="gemini-3.1-flash-lite",
                    contents=full_prompt
                )
                
                reply = response.text
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
                
                # Immediately play faster audio in sync with text output
                speak_text_fast(reply, speed=1.25)

            except Exception as e:
                st.error(f"Error: {e}")
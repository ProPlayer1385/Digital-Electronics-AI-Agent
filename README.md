# 🤖 Digital Electronics AI Agent

An interactive **AI-powered Digital Electronics assistant** built using **Python, Streamlit, and Google Gemini**.

The application helps users perform radix conversions between **Binary, Octal, Decimal, and Hexadecimal** through both **text and voice interaction**. It can validate inputs, provide direct answers, explain conversions step-by-step, and generate spoken responses.

🌐 **[Try the Live Application](https://digital-electronics-ai.streamlit.app/)**

---

## ✨ Features

- 🔢 **Radix Conversion** — Convert between Binary, Octal, Decimal, and Hexadecimal
- 🤖 **AI-Powered Conversations** — Uses Google Gemini for natural language interaction
- 🎙️ **Voice Input** — Ask questions directly using your browser's microphone
- 🔊 **Text-to-Speech** — AI responses can be played back as speech
- 💬 **Conversation History** — Maintains messages throughout the current session
- ✅ **Input Validation** — Identifies invalid digits for the selected number system
- 🧠 **Step-by-Step Explanations** — Provides detailed conversion methods when requested
- 🎨 **Interactive UI** — Custom Streamlit interface with animated gradients and glassmorphism
- 🔐 **Secure API Management** — Gemini API credentials are kept outside the public source code
- ☁️ **Cloud Deployment** — Publicly deployed using Streamlit Community Cloud

---

## 🚀 Live Demo

The application is publicly available here:

### 🌐 [Launch Digital Electronics AI Agent](https://digital-electronics-ai.streamlit.app/)

Try asking:

```text
Convert 101101 from binary to decimal
```

or use the microphone to ask a conversion question through voice input.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core application logic |
| **Streamlit** | Web application and user interface |
| **Google Gemini API** | Generative AI and conversational responses |
| **Google GenAI SDK** | Communication with Gemini models |
| **SpeechRecognition** | Speech-to-text processing |
| **gTTS** | Text-to-speech generation |
| **HTML/CSS** | Custom interface styling and audio playback |
| **Git & GitHub** | Version control and source-code hosting |
| **Streamlit Community Cloud** | Application deployment |

---

## ⚙️ How It Works

The application supports both text and voice interaction.

```text
                    ┌─────────────────────┐
                    │        User         │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   Text / Voice      │
                    │       Input         │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │ Browser Microphone  │
                    │ & Speech-to-Text    │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │ Streamlit Backend   │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   Google Gemini     │
                    │      AI Model       │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │    AI Response      │
                    └──────────┬──────────┘
                               │
                       ┌───────┴───────┐
                       ▼               ▼
                  Text Output     Speech Output
                                      │
                                     gTTS
```

For text input, the prompt can be sent directly to the application.

For voice input, the user's browser captures the audio, which is converted into text before being processed by Gemini.

---

## 🔢 Supported Number Systems

The assistant currently supports conversions involving:

| Number System | Base | Valid Digits |
|---|---:|---|
| Binary | 2 | `0, 1` |
| Octal | 8 | `0–7` |
| Decimal | 10 | `0–9` |
| Hexadecimal | 16 | `0–9, A–F` |

The AI is instructed to validate the supplied digits before performing a conversion.

---

## 🔐 API Key Security

The **Gemini API key is not hardcoded in the public source code**.

For local development, the API key should be stored inside:

```text
.streamlit/secrets.toml
```

with:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

The application accesses it using Streamlit Secrets:

```python
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
```

The actual `secrets.toml` file is excluded from Git using `.gitignore`.

For the deployed application, the API key is stored privately using **Streamlit Community Cloud Secrets**.

> ⚠️ Never commit your actual API key to GitHub.

---

# 💻 Running the Project Locally

## 1. Clone the Repository

```bash
git clone https://github.com/ProPlayer1385/Digital-Electronics-AI-assistant.git
```

Move into the project directory:

```bash
cd Digital-Electronics-AI-assistant
```

---

## 2. Install Dependencies

Make sure Python is installed, then run:

```bash
pip install -r requirements.txt
```

---

## 3. Configure the Gemini API Key

Create the following directory if it does not already exist:

```text
.streamlit/
```

Inside it, create:

```text
secrets.toml
```

Add your Gemini API key:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

---

## 4. Start the Application

Run:

```bash
streamlit run app.py
```

Streamlit should then open the application in your browser.

---

## 📁 Project Structure

```text
Digital-Electronics-AI-assistant/
│
├── app.py
│   └── Main Streamlit application
│
├── requirements.txt
│   └── Python dependencies
│
├── README.md
│   └── Project documentation
│
├── .gitignore
│   └── Prevents private/local files from being committed
│
└── .streamlit/
    └── secrets.toml.example
        └── Example structure for API configuration
```

The real `secrets.toml` file remains private and is **not uploaded to GitHub**.

---

## 💡 Example Queries

You can interact with the assistant using prompts such as:

```text
Convert 101101 from binary to decimal
```

```text
Convert 247 from octal to hexadecimal
```

```text
Convert 3AF from hexadecimal to binary
```

```text
Convert 125 from decimal to binary and explain the steps
```

---

## 🧩 Development & Deployment Challenge

One of the interesting challenges during development was implementing **voice input for a cloud-hosted application**.

The initial version used a local microphone implementation through **PyAudio**. While this worked during local development, it was unsuitable for the deployed Streamlit environment.

The voice-input architecture was therefore changed to use **browser-based audio recording**.

This allows the application to capture audio from the **user's own browser**, process it using speech recognition, and pass the transcribed prompt to Gemini.

```text
Browser Microphone
        ↓
Audio Recording
        ↓
Speech Recognition
        ↓
Text Prompt
        ↓
Gemini
        ↓
AI Response
        ↓
Text + Speech Output
```

This also removed the requirement for PyAudio on the cloud server.

---

## 🗺️ Future Improvements

Some features that could be explored in future versions include:

- Logic gate explanations and simulations
- Boolean algebra simplification
- Karnaugh Map assistance
- Truth-table generation
- Binary arithmetic
- Complement calculations
- Digital Electronics practice questions
- Circuit visualization
- Improved conversational memory
- More advanced voice interaction

The long-term idea is to expand the project from a radix-conversion assistant into a broader **AI learning assistant for Digital Electronics**.

---

## 🔗 Links

🌐 **Live Application:**  
https://digital-electronics-ai.streamlit.app/

💻 **GitHub Repository:**  
https://github.com/ProPlayer1385/Digital-Electronics-AI-assistant

---

## 👨‍💻 Developer

### Archit Kulshrestha

B.Tech Computer Science Engineering  
UPES, Dehradun

Built as a project exploring the integration of **Digital Electronics, Generative AI, voice interaction, and web application development**.

---

## ⭐ Support

If you find this project interesting, consider giving the repository a **star ⭐**.

Feedback, suggestions, and contributions are welcome.

---

**Built with Python 🐍 • Streamlit 🎈 • Google Gemini 🤖**

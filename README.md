# Digital Electronics AI Agent

An interactive **Agentic AI assistant for Digital Electronics**, built with Python, Streamlit and Google's Gemini API.

The application focuses on radix/number-system conversions and supports both text and voice interaction. It can validate number-system inputs, convert between common bases, provide step-by-step explanations on request, and read responses aloud.

## Features

- Binary, Octal, Decimal and Hexadecimal conversion
- Input validation for each radix
- Gemini-powered conversational assistant
- Text-based chat interface
- Voice input using speech recognition
- Text-to-speech responses with gTTS
- Conversation history during the Streamlit session
- Animated gradient and glassmorphism-style Streamlit UI
- Secure API-key handling with Streamlit Secrets

## Tech Stack

- **Python**
- **Streamlit**
- **Google Gemini API (`google-genai`)**
- **SpeechRecognition**
- **gTTS**
- **PyAudio**

## Project Structure

```text
Digital-Electronics-AI-Agent/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
    └── secrets.toml.example
```

Your actual `.streamlit/secrets.toml` file is intentionally excluded from Git so your Gemini API key is never uploaded to GitHub.

## Local Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd Digital-Electronics-AI-Agent
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\\Scripts\\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> `PyAudio` may require platform-specific installation support. If microphone input is unavailable in your deployment environment, the text interface can still be used.

### 4. Configure your Gemini API key

Create this file locally:

```text
.streamlit/secrets.toml
```

Add your **new** Gemini API key:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Never commit this file. It is already included in `.gitignore`.

### 5. Run the application

```bash
streamlit run app.py
```

## Streamlit Community Cloud Deployment

1. Push this project to GitHub.
2. Open Streamlit Community Cloud and create an app from the repository.
3. Select `app.py` as the entry point.
4. Open the app's **Secrets** settings.
5. Add:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

6. Deploy the app.

The API key remains in Streamlit's secret configuration rather than your public GitHub repository.

## Security

Do **not** hardcode API keys in `app.py` or any other tracked source file. If a key has previously been exposed in source code, revoke/regenerate that key before using the project publicly.

## Author

**Archit Kulshrestha**

B.Tech Computer Science student exploring AI/ML, Digital Electronics and interactive technologies.

## Future Improvements

- Logic-gate problem solving
- Boolean algebra simplification
- K-map assistance
- Circuit visualisation
- More Digital Electronics topics beyond radix conversion
- Improved browser-native microphone support for hosted deployments

---

If you find the project useful, feel free to star the repository.

# Voice-Enabled AI Coding Assistant 🌐🔊

This is a terminal-based voice-enabled coding assistant powered by Google's Gemini API and LangChain.

## Features
- Accepts coding questions via microphone.
- Uses Gemini AI to give helpful programming responses.
- Works completely in the terminal.

## Tech Stack
- Python
- LangChain
- Google Gemini API
- SpeechRecognition

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/voice-ai-coding-assistant.git
cd voice-ai-coding-assistant
```

### 2. Create and activate a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API key to `.env`
```
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Run the assistant
```bash
python main.py
```
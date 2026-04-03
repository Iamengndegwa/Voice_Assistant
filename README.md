# 🎙️ AI Voice Assistant

A full-stack conversational AI Voice Assistant built with Python and Flask, powered by **OpenAI GPT-3.5** for intelligent responses, **OpenAI Whisper** for speech-to-text, and **OpenAI TTS** for text-to-speech. Features a sleek dark-mode web interface accessible from any browser.

---

## ✨ Features

- 🎤 **Speech to Text** — Speak directly to the assistant using OpenAI Whisper
- 🤖 **AI Chat** — Powered by OpenAI GPT-3.5-turbo for intelligent responses
- 🔊 **Text to Speech** — Responses read aloud using OpenAI TTS
- 🌙 **Dark Mode UI** — Clean, modern interface
- 🌍 **Network Accessible** — Use on any device on your local network
- 🔒 **Secure** — API keys stored in environment variables, never in code

---

## 🗂️ Project Structure

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/voice-assistant.git
cd voice-assistant
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
Create a `.env` file in the root folder:

---

## ▶️ Running the App
```bash
# Set your API key (Windows PowerShell)
$env:OPENAI_API_KEY="sk-your-key-here"

# Run the server
python Voice_Assistant/server.py
```

Open your browser at: **http://http://127.0.0.1:7860/**

---

## ☁️ Deployment

### Hugging Face Spaces (Free Public URL)
1. Create account at [huggingface.co](https://huggingface.co)
2. Click **New Space → Gradio**
3. Go to **Settings → Secrets** and add `OPENAI_API_KEY`
4. Push your code:
```bash
git remote add space https://huggingface.co/spaces/your-username/voice-assistant
git push space main
```

---

## 🔧 Tech Stack

| Layer | Technology |
|-------|------------|
| UI | HTML, CSS, JavaScript |
| Backend | [Flask](https://flask.palletsprojects.com) |
| AI Chat | [OpenAI GPT-3.5-turbo](https://platform.openai.com) |
| Speech to Text | [OpenAI Whisper](https://platform.openai.com) |
| Text to Speech | [OpenAI TTS](https://platform.openai.com) |
| Language | Python 3.14 |

---

## 🛠️ Troubleshooting

| Error | Fix |
|-------|-----|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `OpenAIError: api_key not set` | Set `$env:OPENAI_API_KEY` in terminal or add to `.env` |
| `RateLimitError 429` | Add billing credits at [platform.openai.com/billing](https://platform.openai.com/billing) |
| `git not recognized` | Install Git from [git-scm.com](https://git-scm.com/download/win) and restart terminal |

---

## 🔐 Security Notes

- Never hardcode your API key in any file
- Always use environment variables or a `.env` file
- Rotate your API key immediately if it is ever exposed publicly

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🙏 Acknowledgements

- [OpenAI](https://openai.com) for GPT, Whisper and TTS APIs
- [Flask](https://flask.palletsprojects.com) for the backend framework
- [Hugging Face](https://huggingface.co) for free model hosting

# Jarvis (Just A Rather Very Intelligent System)

Jarvis is a Python-based personal voice assistant with a cool graphical interface. It listens for your voice commands and performs a variety of computer tasks — from searching the web to opening applications, sending emails, reporting weather, taking notes, and more.

## 🚀 Features

- 🎤 **Voice Interaction:** Greets user, tells time/date, responds to voice commands
- 🌐 **Web & Search:** Google search, Wikipedia summaries, news, IP address lookup
- 📧 **Communication:** Sends emails with subject & content via voice input
- 📅 **Productivity:** Opens applications, notes, system stats, Google Calendar events
- 🔊 **Media:** Plays songs on YouTube, music streaming
- 🧠 **Knowledge:** Answers questions via WolframAlpha, solves math queries
- 🖼️ **System Utilities:** Screenshots, hide/unhide files, switch windows
- 📊 **System Info:** CPU, RAM, and battery status
- 🖥️ **GUI Support:** Interactive interface for better user experience

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Arpitgarg07/Jarvis.git
cd Jarvis
```

### 2. Create `config.py` File

Inside the `Jarvis/config` directory, create a `config.py` file and add your credentials:

```python
email = "<your_email>"
email_password = "<your_email_password>"
wolframalpha_id = "<your_wolframalpha_id>"
```

### 3. Setup Python Environment (Python 3.8 Recommended)

```bash
conda create -n jarvis python=3.8
conda activate jarvis
# OR
python3.8 -m venv jarvis
source jarvis/bin/activate  # On Windows use: jarvis\Scripts\activate
```

### 4. Install Requirements

```bash
pip install -r requirements.txt
```

> **Note:** You may need to install `PyAudio` manually on Windows. Download from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).

### 5. Get API Keys

- [OpenWeatherMap](https://openweathermap.org/api)
- [WolframAlpha](https://developer.wolframalpha.com/)
- [Google Calendar API](https://developers.google.com/calendar)

Add these keys to your `config.py`.

### 6. Run the Assistant

```bash
python main.py
```

---

## 💡 Usage Examples

Once running, try voice commands like:

- “What’s the time?”
- “Open YouTube”
- “Search Wikipedia for Python”
- “Send email to Arpit”
- “What’s the weather in Jaipur?”
- “Play song on YouTube”
- “Take screenshot named jarvis.png”
- “Hide files in Documents”

---

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add feature'`)
5. Push to the branch (`git push origin feature-name`)
6. Create a Pull Request

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Credits

- Developed by [Arpit Garg](https://github.com/Arpitgarg07)
- Based on the original J.A.R.V.I.S. project by [Atharva Ingle (Gladiator07)](https://github.com/Gladiator07)
- GUI and libraries credit to respective authors

---

⭐ If you like this project, consider starring the repo and sharing it!

<!-- # Jarvis (Just A Rather Very Intelligent System)

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
- GUI and libraries credit to respective authors

---

⭐ If you like this project, consider starring the repo and sharing it! -->
<!-- <p align="center">
  <img src="https://github.com/Arpitgarg07/Jarvis/blob/main/docs/jarvis-logo.png" alt="Jarvis Logo" width="200"/>
</p> -->

<h1 align="center">Jarvis - Just A Rather Very Intelligent Assistant 🤖</h1>

<p align="center">
  <strong>An open-source Python-based personal voice assistant with face recognition security and intelligent automation capabilities.</strong>
  <br />
  <br />
  <a href="#-getting-started-in-under-5-minutes"><strong>🚀 Get Started</strong></a>
  ·
  <a href="https://github.com/Arpitgarg07/Jarvis/issues"><strong>🐛 Report a Bug</strong></a>
  ·
  <a href="https://github.com/Arpitgarg07/Jarvis/issues"><strong>✨ Request a Feature</strong></a>
</p>

<p align="center">
  <a href="https://github.com/Arpitgarg07/Jarvis/stargazers"><img src="https://img.shields.io/github/stars/Arpitgarg07/Jarvis?style=for-the-badge&logo=github&color=FFDD00" alt="Stars"></a>
  <a href="https://github.com/Arpitgarg07/Jarvis/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Arpitgarg07/Jarvis?style=for-the-badge&color=00BFFF" alt="License"></a>
  <a href="https://github.com/Arpitgarg07/Jarvis/network/members"><img src="https://img.shields.io/github/forks/Arpitgarg07/Jarvis?style=for-the-badge&logo=github&color=90EE90" alt="Forks"></a>
</p>

---

## 🌟 The Vision: Your Secure Personal AI Assistant

**Jarvis** transforms your computer into an intelligent companion that not only responds to voice commands but also recognizes your face for secure access. Built with Python and powered by advanced AI libraries, Jarvis combines the convenience of voice interaction with the security of biometric authentication.

Unlike commercial assistants, Jarvis runs entirely on your machine, giving you complete control over your data and privacy while providing powerful automation capabilities.

### 🔥 Core Features

*   **🎤 Voice Interaction:** Natural speech recognition with contextual responses and greetings
*   **👤 Face Recognition Security:** Biometric authentication with automatic screenshots for security
*   **🌐 Web Intelligence:** Google search, Wikipedia summaries, news updates, and IP lookup
*   **📧 Email Automation:** Voice-controlled email composition and sending
*   **🖥️ System Control:** Application launching, file management, screenshots, and system monitoring  
*   **🎵 Entertainment Hub:** YouTube control, music playback, and media management
*   **🧠 Advanced Computing:** WolframAlpha integration for complex calculations and queries
*   **⏰ Smart Scheduling:** Alarms, reminders, task management, and focus mode
*   **📱 Communication:** WhatsApp messaging and call automation via Twilio
*   **🎮 Interactive Features:** Built-in games like Rock Paper Scissors
*   **🌍 Multilingual Support:** Translation capabilities with voice output
*   **📊 System Monitoring:** Battery status, performance metrics, and notifications

---

## 🏗️ System Architecture: Security-First Design

Jarvis implements a multi-layered architecture with security at its core:

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    Jarvis System Architecture                             │
├────────────────────────────────────────────────────────────────────────────┤
│ 🔒 SECURITY LAYER                                                          │
│ ┌──────────────────────┐ ┌──────────────────────┐ ┌──────────────────────┐ │
│ │    Face Training     │ │   Face Detection     │ │ Access Control &     │ │
│ │      (OpenCV)        │ │       (LBPH)         │ │    Screenshots       │ │
│ └──────────────────────┘ └──────────────────────┘ └──────────────────────┘ │
│                                      │                                     │
│                                      ▼                                     │
│ 🎤 INTERACTION LAYER                                                     │
│ ┌──────────────────────┐ ┌──────────────────────┐ ┌──────────────────────┐ │
│ │      Speech          │ │      Command         │ │      Response        │ │
│ │    Recognition       │ │     Processing       │ │     Generation       │ │
│ │    (Google API)      │ │      Engine          │ │      (pyttsx3)       │ │
│ └──────────────────────┘ └──────────────────────┘ └──────────────────────┘ │
│                                      │                                     │
│                                      ▼                                     │
│ ⚙️ SERVICE LAYER                                                         │
│ ┌──────────────────────┐ ┌──────────────────────┐ ┌──────────────────────┐ │
│ │        Web           │ │       Email          │ │       System         │ │
│ │      Services        │ │        SMTP          │ │       Control        │ │
│ └──────────────────────┘ └──────────────────────┘ └──────────────────────┘ │
│ ┌──────────────────────┐ ┌──────────────────────┐ ┌──────────────────────┐ │
│ │       Alarms &       │ │       Games &        │ │     Translation      │ │
│ │      Reminders       │ │        Jokes         │ │       Engine         │ │
│ └──────────────────────┘ └──────────────────────┘ └──────────────────────┘ │
│ ┌──────────────────────┐                                                    │
│ │      Wolfram         │                                                    │
│ │       Alpha          │                                                    │
│ └──────────────────────┘                                                    │
└────────────────────────────────────────────────────────────────────────────┘

```

---

## 🚀 The Tech Stack: Proven & Powerful

| Component              | Technology                     | Purpose                                                                                    |
| ---------------------- | ------------------------------ | ------------------------------------------------------------------------------------------ |
| **Speech Recognition** | **Google Speech API**          | High-accuracy voice command processing with natural language understanding                  |
| **Text-to-Speech**     | **pyttsx3**                    | Offline voice synthesis with customizable speech rates and voices                         |
| **Face Recognition**   | **OpenCV + LBPH**              | Secure biometric authentication with Local Binary Patterns Histograms                     |
| **GUI Framework**      | **Tkinter + PIL**              | Native cross-platform interface with animated GIF support                                 |
| **Web Automation**     | **requests + BeautifulSoup**   | Intelligent web scraping and API interactions                                             |
| **System Control**     | **pyautogui + psutil**         | Complete system automation and performance monitoring                                      |
| **Email Service**      | **smtplib**                    | Secure email sending with Gmail integration                                               |
| **Messaging**          | **pywhatkit + Twilio**         | WhatsApp automation and phone call capabilities                                           |
| **Knowledge Engine**   | **WolframAlpha API**           | Advanced mathematical and factual query processing                                        |
| **Translation**        | **googletrans + gTTS**         | Multi-language translation with voice output                                              |

---

## 🛠️ Getting Started in Under 5 Minutes

### Prerequisites

1.  **Python 3.8+:** [Download here](https://www.python.org/downloads/)
2.  **Webcam:** Required for face recognition security
3.  **Microphone:** For voice commands
4.  **Internet Connection:** For API services

### Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Arpitgarg07/Jarvis.git
    cd Jarvis
    ```

2.  **Install Dependencies:**
    ```bash
    # Run the automatic installer
    python installer.py
    
    # OR install manually
    pip install -r requirements.txt
    ```
    > **Note:** On Windows, you may need to install PyAudio manually from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).

3.  **Set Up Face Recognition (Security):**
    ```bash
    # Generate face samples (10 photos)
    python "Sample generator.py"
    
    # Train the recognition model
    python "Model Trainer.py"
    ```

4.  **Configure API Keys:**
    Update the following files with your credentials:
    
    **For WolframAlpha (Calculatenumbers.py):**
    ```python
    apikey = "YOUR_WOLFRAMALPHA_API_KEY"
    ```
    
    **For News (NewsRead.py):**
    ```python
    # Replace the API key in the URLs
    apiKey=YOUR_NEWS_API_KEY
    ```
    
    **For Email (sendemail.py):**
    ```python
    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"
    ```

5.  **🎉 Launch Jarvis:**
    ```bash
    python Jarvismain.py
    ```

6.  **Activate Your Assistant:**
    Say **"Wake up"** to start interacting with Jarvis!

---

💡 Voice Commands: What Jarvis Can Do
🎤 Basic Commands

"Wake up" , "Go to sleep" - Control Jarvis
"Hello" ,"What's the time?" - Basic interaction
"Google search [topic]" , "Wikipedia [topic]" - Web search
"What's the news?" ,"What's my IP address?" - Information

🖥️ System & Productivity

"Open [app]" , "Take screenshot" - System control
"Set an alarm" , "Remind me" - Time management
"Focus mode" , "Show my focus" - Productivity tracking
"Battery status" , "Internet speed test" - System info

📧 Communication & Entertainment

"Write an email" , "WhatsApp message" - Communication
"Play playlist" , "Tell me a joke" - Entertainment
"Calculate [math]" , "Translate [text]" - Smart features
"Open game" , "Flip a coin" - Interactive fun

---

## 🔧 Advanced Configuration

### Face Recognition Setup
1. Run `Sample generator.py` to capture 10 face samples
2. Execute `Model Trainer.py` to create recognition model
3. Update the `names` list in `Jarvismain.py` with your name
4. Adjust `id` variable to match your assigned number

### Focus Mode
- Blocks distracting websites during work sessions
- Tracks productivity time in `focus.txt`
- Generates focus graphs with `FocusGraph.py`
- Requires administrator privileges on Windows

### WhatsApp Integration
- Update `contact_dict` in `Jarvismain.py` with your contacts
- Uses `pywhatkit` for automated messaging
- Supports both manual and automated message scheduling

### Email Configuration
- Use Gmail App Passwords for security
- Update recipient mappings in `sendemail.py`
- Supports voice-to-text email composition

---

## 🌟 Unique Features

### 🔒 **Security First**
- Biometric face recognition with OpenCV
- Automatic security screenshots for unknown faces
- Optional password protection
- Local data processing for privacy

### 🧠 **Smart Automation**
- Context-aware command processing
- Natural language understanding
- Intelligent system control
- Productivity tracking and analytics

### 🎯 **Focus Mode**
- Website blocking during work sessions
- Productivity time tracking
- Visual analytics with matplotlib
- Administrative control for system-level blocking

### 🎮 **Interactive Entertainment**
- Built-in games (Rock Paper Scissors)
- Joke telling with pyjokes
- Coin flipping with sound effects
- Interactive voice responses

---

## 🤝 Contributing to Jarvis

We welcome contributions! Here's how you can help:

### 🌟 **Ways to Contribute**
- **🐛 Bug Fixes:** Improve reliability and fix issues
- **✨ New Commands:** Add more voice command capabilities  
- **🔧 Hardware Support:** Expand device compatibility
- **🌍 Localization:** Add support for more languages
- **📱 Integrations:** Connect with more services and APIs
- **🎨 UI Improvements:** Enhance the visual interface

### 📝 **Getting Started**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Test your changes thoroughly
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

---


## 🔑 Required API Keys

### Free APIs (Recommended)
- **WolframAlpha:** [Get API Key](https://developer.wolframalpha.com/) - 2000 queries/month free
- **News API:** [Get API Key](https://newsapi.org/) - 1000 requests/day free
- **OpenWeatherMap:** [Get API Key](https://openweathermap.org/api) - 1000 calls/day free

### Optional Paid APIs
- **Twilio:** For phone call functionality
- **Google Calendar API:** For advanced calendar integration

---

## 📁 Project Structure

```
Jarvis/
├── Jarvismain.py              # Main application with face recognition
├── INTRO.py                   # Animated startup screen
├── GreetMe.py                 # Greeting functionality
├── Calculatenumbers.py        # WolframAlpha integration
├── Dictapp.py                # System control functions
├── SearchNow.py              # Web search capabilities
├── NewsRead.py               # News reading functionality
├── Whatsapp.py               # WhatsApp integration
├── Translator.py             # Translation services
├── FocusMode.py              # Productivity website blocking
├── FocusGraph.py             # Focus time visualization
├── battery.py                # Battery monitoring
├── game.py                   # Rock Paper Scissors game
├── joke.py                   # Joke functionality
├── alarm.py                  # Alarm system
├── reminder.py               # Reminder notifications
├── sendemail.py              # Email functionality
├── Location.py               # Location services
├── Sample generator.py       # Face recognition training
├── Model Trainer.py          # Face recognition model
├── installer.py              # Dependency installer
├── keyboard.py               # Volume control
├── sendcall.py               # Twilio call integration
└── Various text files        # Data storage and configuration
```

---

## 🛡️ Privacy & Security

**Jarvis prioritizes your privacy:**

- **Local Processing:** Face recognition and most operations run locally
- **Encrypted Storage:** Sensitive data encrypted on your machine  
- **API Control:** You choose which external services to use
- **Open Source:** Complete transparency - inspect every line of code
- **No Tracking:** Zero telemetry or user data collection
- **Biometric Security:** Face recognition prevents unauthorized access

---

## 🌟 Contributors

Thanks to these amazing people who make Jarvis better:

<a href="https://github.com/Arpitgarg07/Jarvis/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Arpitgarg07/Jarvis" />
</a>

---

## 💬 Community & Support

- **💬 Discussions:** [GitHub Discussions](https://github.com/Arpitgarg07/Jarvis/discussions)
- **🐛 Bug Reports:** [Issues](https://github.com/Arpitgarg07/Jarvis/issues)
- **📧 Email:** [Contact Arpit](mailto:contact@arpitgarg.com)

---

## 📜 License

This project is freely available under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Tony Stark/Iron Man:** For the inspiration behind the name and vision
- **OpenCV Community:** For powerful computer vision tools
- **Python Community:** For the amazing libraries that power Jarvis
- **Contributors:** Everyone who helps improve this project
- **Users:** Thank you for choosing Jarvis as your AI assistant

---

<div align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
  <p><strong>🤖 "Sometimes you gotta run before you can walk." - Tony Stark</strong></p>
  <p>Built with ❤️ and Python. Secure AI assistance for everyone.</p>
  <img src="https://komarev.com/ghpvc/?username=Arpitgarg07-Jarvis&label=Project%20Views&color=00BFFF&style=flat" alt="Project views" />
</div>
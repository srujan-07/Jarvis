#!/usr/bin/env python3
"""
Jarvis Quick Setup Script
Automates the entire Jarvis setup process in under 5 minutes
"""

import os
import sys
import subprocess
import platform

def print_banner():
    print("""
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║                    JARVIS - Quick Setup Script                              ║
    ║                    Getting Started in Under 5 Minutes                       ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
    """)

def check_python_version():
    """Check if Python 3.8+ is installed"""
    print("🔍 Checking Python version...")
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8+ is required!")
        print("📥 Download Python from: https://www.python.org/downloads/")
        sys.exit(1)
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")

def install_dependencies():
    """Install required dependencies"""
    print("\n📦 Installing dependencies...")
    try:
        # Try automatic installer first
        if os.path.exists("installer.py"):
            print("🔄 Running automatic installer...")
            subprocess.run([sys.executable, "installer.py"], check=True)
        else:
            # Fallback to requirements.txt
            if os.path.exists("requirements.txt"):
                print("🔄 Installing from requirements.txt...")
                subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
            else:
                print("🔄 Installing core packages...")
                packages = [
                    "pyttsx3", "SpeechRecognition", "opencv-python", "requests",
                    "pyautogui", "speedtest-cli", "numpy", "beautifulsoup4",
                    "plyer", "nltk", "pygame", "psutil", "wolframalpha",
                    "Pillow", "pyjokes", "pynput", "googletrans", "gtts",
                    "pywhatkit", "wikipedia", "twilio", "playsound", "mouse"
                ]
                for package in packages:
                    subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Error installing dependencies. Please install manually.")
        return False
    return True

def create_directories():
    """Create necessary directories"""
    print("\n📁 Creating directories...")
    directories = ["samples", "trainer"]
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✅ Created {directory}/ directory")

def setup_face_recognition():
    """Guide user through face recognition setup"""
    print("\n🔒 Setting up Face Recognition Security...")
    print("This step is important for security!")
    
    response = input("Do you want to set up face recognition now? (y/n): ").lower()
    if response == 'y':
        print("\n📸 Step 1: Generating face samples...")
        print("⚠️  Look at your camera and follow the instructions")
        
        try:
            subprocess.run([sys.executable, "Sample generator.py"], check=True)
            
            print("\n🧠 Step 2: Training recognition model...")
            subprocess.run([sys.executable, "Model Trainer.py"], check=True)
            print("✅ Face recognition setup complete!")
            
        except subprocess.CalledProcessError:
            print("❌ Face recognition setup failed. You can run this manually later:")
            print("   python 'Sample generator.py'")
            print("   python 'Model Trainer.py'")
    else:
        print("⚠️  Skipping face recognition setup.")
        print("   You can set it up later by running:")
        print("   python 'Sample generator.py'")
        print("   python 'Model Trainer.py'")

def show_api_setup():
    """Show API setup instructions"""
    print("\n🔑 API Keys Setup (Required for full functionality):")
    print("─" * 60)
    print("1. WolframAlpha API (for calculations):")
    print("   🌐 Get key: https://developer.wolframalpha.com/")
    print("   📝 Edit: Calculatenumbers.py")
    print("   💾 Replace: apikey = 'YOUR_WOLFRAMALPHA_API_KEY'")
    print()
    print("2. News API (for news updates):")
    print("   🌐 Get key: https://newsapi.org/")
    print("   📝 Edit: NewsRead.py")
    print("   💾 Replace: apiKey=YOUR_NEWS_API_KEY")
    print()
    print("3. Email Setup (for sending emails):")
    print("   📝 Edit: sendemail.py")
    print("   💾 Replace: sender_email = 'your_email@gmail.com'")
    print("   💾 Replace: sender_password = 'your_app_password'")
    print("   ⚠️  Use App Password for Gmail: https://support.google.com/accounts/answer/185833")

def main():
    """Main setup function"""
    print_banner()
    
    # Check Python version
    check_python_version()
    
    # Install dependencies
    if not install_dependencies():
        return
    
    # Create directories
    create_directories()
    
    # Setup face recognition
    setup_face_recognition()
    
    # Show API setup
    show_api_setup()
    
    # Final instructions
    print("\n" + "=" * 80)
    print("🎉 SETUP COMPLETE!")
    print("=" * 80)
    print("🚀 To start Jarvis:")
    print("   python Jarvismain.py")
    print()
    print("🗣️  To activate:")
    print("   Say 'Wake up' to start interacting with Jarvis!")
    print()
    print("📚 Voice Commands Examples:")
    print("   • 'What's the time?'")
    print("   • 'Open YouTube'")
    print("   • 'Search Wikipedia for Python'")
    print("   • 'Tell me a joke'")
    print("   • 'Take screenshot'")
    print()
    print("⚠️  Don't forget to setup your API keys for full functionality!")
    print("=" * 80)

if __name__ == "__main__":
    main()

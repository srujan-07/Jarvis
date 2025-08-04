import pyttsx3 
import speech_recognition as sr 
import datetime
import random
import sys

# Initialize text-to-speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 185)

def Speak(audio):
    engine.say(audio)
    engine.runAndWait()

def TakeCommand():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 300
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            
        print("🔄 Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"✅ You said: {query}")
        return query
        
    except sr.WaitTimeoutError:
        print("⏰ No speech detected...")
        return "None"
    except sr.UnknownValueError:
        print("❓ Could not understand...")
        return "None"
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return "None"

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        Speak("Good Morning, Sir.")
    elif hour >= 12 and hour <= 18:
        Speak("Good Afternoon, Sir.")   
    else:
        Speak("Good Evening, Sir.")
    Speak("I am Jarvis. How can I help you?")

if __name__ == "__main__":
    print("🤖 JARVIS - Simple Mode (No Face Recognition)")
    print("=" * 50)
    
    Speak("Hello! This is Jarvis simple mode. Say WAKE UP to begin.")
    print("💬 Say 'WAKE UP' to activate Jarvis...")
    
    while True:
        query = TakeCommand()
        
        if query == "None":
            continue
            
        query = query.lower()
        
        if "wake up" in query:
            greetMe()
            print("🎤 Jarvis activated! Try these commands:")
            print("- 'hello' or 'hi'")
            print("- 'time' or 'what time is it'")
            print("- 'calculate 2 plus 3'")
            print("- 'exit' to quit")
            
            while True:
                query = TakeCommand()
                
                if query == "None":
                    continue
                    
                query = query.lower()
                
                if "go to sleep" in query:
                    Speak("Ok sir, you can call me anytime.")
                    break
                    
                elif "hello" in query or "hi" in query or "hey" in query:
                    Speak("Hello sir, How are you!")
                    
                elif "how are you" in query:
                    Speak("Perfect sir!")
                    
                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"🕐 Current time: {strTime}")
                    Speak(f"Sir, the time is {strTime}")
                    
                elif "calculate" in query:
                    Speak("I heard a calculation request. The full calculator needs WolframAlpha API.")
                    print("🧮 Calculation feature detected")
                    
                elif "exit" in query or "quit" in query:
                    Speak("Goodbye!")
                    sys.exit()
                    
                else:
                    print(f"🤔 Command: {query}")
                    Speak("I heard you, but I don't understand that command yet. Try hello, time, or calculate.")
                    
        elif "exit" in query or "quit" in query:
            Speak("Goodbye!")
            break
            
        else:
            print(f"💤 Waiting for wake up command... (heard: {query})")

import requests
import json
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",185)

def Speak(audio):
    engine.say(audio)
    engine.runAndWait()

def TakeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # r.energy_threshold = 200
        audio = r.listen(source,0,4)

    try:
        print("Understanding...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Master said: {query}\n")

    except Exception as e:
        print("Say that again please...") 
        return "None"
    return query

#! In latestnews we use in link after "=" sign our api key. 
def latestnews():
    # NewsAPI key configured
    API_KEY = "0af0f013c3bb42ee97812d104e8a1bfc"
    
    api_dict = {"business" : f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={API_KEY}",
            "entertainment" : f"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey={API_KEY}",
            "health" : f"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey={API_KEY}",
            "science" : f"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey={API_KEY}",
            "sports" : f"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={API_KEY}",
            "technology" : f"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey={API_KEY}"
}

    content = None
    url = None
    Speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = TakeCommand().lower()

    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    Speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        Speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")
        Speak("If you want to continue speak 'other' else 'stop'")

        a = TakeCommand().lower()
        if str(a) == "other":
            pass
        elif str(a) == "stop":
            break
        
    Speak("thats all")

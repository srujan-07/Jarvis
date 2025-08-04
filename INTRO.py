from tkinter import *
import time
import pygame
from pygame import mixer
import pyautogui

mixer.init()

root = Tk()
root.geometry("1100x600")
root.configure(bg='black')
root.title("J.A.R.V.I.S - Just A Rather Very Intelligent System")

def play_intro():
    root.lift()
    root.attributes("-topmost", True)
    
    # Create main label for title
    title_label = Label(root, text="J.A.R.V.I.S", font=("Arial", 48, "bold"), 
                       fg="cyan", bg="black")
    title_label.place(x=400, y=200)
    
    subtitle_label = Label(root, text="Just A Rather Very Intelligent System", 
                          font=("Arial", 16), fg="white", bg="black")
    subtitle_label.place(x=350, y=280)
    
    status_label = Label(root, text="Initializing...", 
                        font=("Arial", 14), fg="green", bg="black")
    status_label.place(x=500, y=350)
    
    root.update()
    
    # Try to play audio if jarvis.mp3 exists
    try:
        mixer.music.load("jarvis.mp3")
        mixer.music.play()
    except:
        print("Audio file jarvis.mp3 not found, continuing without audio...")
    
    # Simulate loading sequence
    loading_messages = [
        "Loading neural networks...",
        "Initializing voice recognition...",
        "Connecting to APIs...",
        "Face recognition ready...",
        "System online!"
    ]
    
    for i, message in enumerate(loading_messages):
        status_label.config(text=message)
        root.update()
        time.sleep(2)
    
    # Final message
    final_label = Label(root, text="Say 'WAKE UP' to activate", 
                       font=("Arial", 18, "bold"), fg="yellow", bg="black")
    final_label.place(x=420, y=400)
    root.update()
    
    time.sleep(3)
    root.quit()

play_intro()
root.mainloop()


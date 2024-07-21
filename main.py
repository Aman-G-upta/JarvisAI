import speech_recognition as sr
import webbrowser
import pyttsx3
import music
import requests


recognizer = sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(tell):
    if "open google" in tell.lower():
        webbrowser.open("https://google.com")

    elif "open linkedin" in tell.lower():
        webbrowser.open("https://linkedin.com")

    elif "open youtube" in tell.lower():
        webbrowser.open("https://youtube.com")

    elif "open facebook" in tell.lower():
        webbrowser.open("https://facebook.com") 

    elif tell.lower().startswith("play"):
        song=tell.lower().split(" ")[1]   
        link=music.music[song]
        webbrowser.open(link)


# if __name__ == "__main__":
speak("Initializing jarvis")
while True:
    # Obtain audio from the microphone
    r= sr.Recognizer()
    
    print("Recognizing..........")
    try:
        # Listening for the wake word jarvis
        with sr.Microphone() as source:
            print("Listening...........")
            audio= r.listen(source,timeout=2,phrase_time_limit=1)
        word=r.recognize_google(audio)
        if (word.lower()=="jarvis"):
            speak("YA")
            with sr.Microphone() as source:
                print("Jarvis Active..........")
                audio= r.listen(source,timeout=2,phrase_time_limit=1)    
                command = r.recognize_google(audio)
                print(command)
                processcommand(command)
    except Exception as e:
        print(e)


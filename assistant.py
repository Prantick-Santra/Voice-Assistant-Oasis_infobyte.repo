import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if 0<=hour<12:
        print("Good Morning Sir")
        speak("Good Morning Sir")
    elif hour==12:
        print("Good Noon Sir")
        speak("Good Noon Sir")
    elif 12<hour<18:
        print("Good Afternoon Sir")
        speak("Good Afternoon Sir")
    else:
        print("Good Evening Sir")
        speak("Good Evening Sir")
    print("I am FRIDAY, your personal assistant, how may I help you?")
    speak("I am FRIDAY, your personal assistant, how may I help you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.energy_threshold=500
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say That again please")
        speak("Say That again please")
        return "None"
    return query

if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()
        # Logics for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'what is your name' in query:
            print("I am FRIDAY sir, an AI assistant, created by Mr. Prantick Santra. I am here to help you, in your work")
            speak("I am FRIDAY sir, an AI assistant, created by Mr. Prantick Santra. I am here to help you, in your work")
        
        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')
        elif 'open google' in query:
            webbrowser.open('https://www.google.com/')
        elif 'open google sheet' in query:
            webbrowser.open("https://docs.google.com/spreadsheets/u/0/?pli=1")
        elif 'open google doc' in query:
            webbrowser.open('https://docs.google.com/document/u/0/')
        elif 'open google slide' in query:
            webbrowser.open('https://docs.google.com/presentation/u/0/')
        elif 'open google clssroom' in query:
            webbrowser.open('https://classroom.google.com/')
        elif 'open google map' in query:
            webbrowser.open('https://www.google.com/maps/@22.5469393,87.9236737,3222m/data=!3m1!1e3?authuser=0&entry=ttu')
        elif 'open gmail' in query:
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
        elif 'open gpt 3.5' in query:
            webbrowser.open('https://chat.openai.com/')
        elif 'open AI' in query:
            webbrowser.open('https://bard.google.com/chat')
        elif 'open bing' in query:
            webbrowser.open('https://www.bing.com/search?form=NTPCHB&q=Bing+AI&showconv=1')
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
        elif 'open linkedin' in query:
            webbrowser.open("https://www.linkedin.com/feed/")
        elif 'open naukri' in query:
            webbrowser.open("https://www.naukri.com/mnjuser/homepage")


        elif 'play a music' in query:
            music_dir="D:\\Music"
            songs=os.listdir(music_dir)
            song=random.randint(0,len(songs))
            print(songs[song])
            os.startfile(os.path.join(music_dir,songs[song]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, The time is {strTime}")
            speak(f"Sir, The time is {strTime}")


        elif 'open code' in query:
            codepath="C:\\Users\\santr\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'open microsoft edge' in query:
            edgepath="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(edgepath)
        elif 'open brave' in query:
            bravepath="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(bravepath)
        elif 'open zoom' in query:
            zoompath="C:\\Users\\santr\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoompath)
        elif 'quite' or 'fuck off' or 'Shut Down' in query:
            print("Thank you sir, if you have any more command, feel free to reach out")
            speak("Thank you sir, if you have any more command, feel free to reach out")
            break

import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

friday = pyttsx3.init()
voice = friday.getProperty("voices")
friday.setProperty("voice",voice[1].id)

def speak(audio):
    print("F.R.I.D.A.Y: " + audio)
    friday.say(audio)
    friday.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)

def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir")
    if hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    if hour >= 18 and hour < 24:
        speak("Good Night Sir")
    speak("How can I help you?")

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language= "en")
        print("Tony Hải: " + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command")
        query = str(input("Your order is: "))
    return query

if __name__ == "__main__":
    welcome()
    while True:
        query = command().lower()
        if "google" in query:
            speak("What should I search boss?")
            search = command().lower()
            url = f"https://www.google.com.vn/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on Google")
        if "duolingo" or "Duolingo" in query:
            search = command().lower()
            url = f"https://www.duolingo.com/learn"
            wb.get().open(url)
            speak("Here is Duolingo")
        if "youtube" in query:
            speak("What should I search boss?")
            search = command().lower()
            url = f"https://www.youtube.com/results?search_query={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on Youtube")
        elif "time" in query:
            time()
        elif "quit" or "bye" in query:
            speak("Friday is quitting sir. Goodbye boss")
            quit()
            
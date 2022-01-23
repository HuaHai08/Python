import weakref
import speech_recognition
import pyttsx3
import datetime
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain =""
voices = robot_mouth.getProperty('voices') 
robot_mouth.setProperty('voice', voices[0].id)

while True:
    with speech_recognition.Microphone() as mic:
        robot_ear.adjust_for_ambient_noise(mic)
        print("Robot David: I'm Listening")
        audio = robot_ear.listen(mic)

    print("Robot David: ")

    try: 
        you = robot_ear.recognize_google(audio, language='vi-VN')
    except: 
        you = ""

    print("You: " + you)

    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "Xin chào" in you:
        robot_brain = "Chào Hải"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you :
        now = datetime.now()
        current_time = now.strftime("%H hours, %M minutes, %S seconds")
    elif "president" in you:
        robot_brain = "Nguyễn Xuân Phúc"
    elif "bye" in you:
        robot_brain = "Bye Hải"
        print("Robot David: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I'm fine thank you and you"

    print("Robot David: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
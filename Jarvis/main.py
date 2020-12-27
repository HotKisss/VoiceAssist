import sys
import speech_recognition as sr
import os
import pyttsx3
import subprocess



def talk(words):
    if words != '':
        engine = pyttsx3.init()
        engine.say(words)
        engine.runAndWait()


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, 1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language = "ru-RU").lower()
    except sr.UnknownValueError:
        task = command()

    return task

def make_something(task):
   
    if 'алан' in task:
        subprocess.Popen(['python', r'F:\Repository\VoiceAssist\Jarvis\jarvis.py'])
        exit(0)

speak_engine = pyttsx3.init()
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[3].id)

while 1:
    make_something(command())
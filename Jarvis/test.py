import pyttsx3
import webbrowser
import time
import pickle
from selenium import webdriver

engine = pyttsx3.init()
engine.say("красава")
engine.runAndWait()

voices = engine.getProperty('voices')
for voice in voices:
    print(voice.name)

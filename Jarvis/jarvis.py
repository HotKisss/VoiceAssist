# Голосовой ассистент КЕША 1.0 BETA
import os
import time
import webbrowser
from threading import Timer
import speech_recognition as sr
import win32com.client as wincl
from fuzzywuzzy import fuzz
import pyttsx3
import subprocess
import datetime
import random 
#import files
import jokes
import options
import music
import message


opts = options.opts
messageState = " "
# функции
def speak(what):
    print(what)
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer, audio):
    try:
        global messageState
        global voice
        voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
        print("[log] Распознано: " + voice)
        sendTheMessage()
        #if voice.startswith(opts["alias"]):
            
        cmd = voice
 
        for x in opts['alias']:
            cmd = cmd.replace(x, "").strip()
            
        for x in opts['tbr']:
            cmd = cmd.replace(x, "").strip()
            
            # распознаем и выполняем команду
        cmd = recognize_cmd(cmd)
        execute_cmd(cmd['cmd'])
 
    except sr.UnknownValueError:
        pass
 
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 50}
    for c,v in opts['cmds'].items():
 
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    
    return RC
 
def execute_cmd(cmd):
    try:
        if 'ctime' in cmd:
            # сказать текущее время
            now = datetime.datetime.now()
            speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

        elif 'hello' in cmd:
            z = ["Приветствую тебя", "Хай чувак", "Ку", "Привет, присаживайся к огоньку", "О, привет, я уже соскучился по тебе"]
            x = random.choice(z)
            speak(x)
            
        #Отправка сообщения
        elif 'message' in cmd:
            global messageState
            message.sendMessage()
            speak("Кому отправить сообщение?")
            messageState = "whoState"
            print(messageState)



        elif 'quit' in cmd:
            z = ["Пока друг", "Надеюсь ещё увидимся", "Бб", "Аривидэрчи", "Покасики", "Чеши бока ёпта, давай бывай"]
            speak(random.choice(z))
            shutDownThisProgramAndOpenMain()


        elif 'music' in cmd:
            global musicOn
            musicOn = True
            speak("Вы хотите чтобы я включил вам музыку?")

        elif 'yes' in cmd:
            try:
                if musicOn == True:
                    musicOn = False
                    speak("Хорошо, включаю музыку")
                    music.playMusic()
            except:
                pass
        
        elif 'skipSong' in cmd:
            speak("Скипаю")
            music.skipSong()
        
        elif 'spotify' in cmd:
            speak("Открываю спотифай")
            os.system(r"F:\Something\\Spotify\\Spotify.exe")
        
        
        elif 'vk' in cmd:
            webbrowser.open('https://vk.com/huligun1488', new=2) 
        

        elif 'steam' in cmd:
            speak("Открываю стим")
            os.system(r"D:\Games\\steam.exe")
        
        elif 'rl' in cmd:
            speak("Открываю рокет лигу")
            os.system(r"D:\Games\\steamapps\\common\\rocketleague\\Binaries\\Win64\\RocketLeague.exe")
        
        elif 'csgo' in cmd:
            speak("Открываю каэс")
            os.system(r"D:\Games\\steamapps\\common\\Counter-Strike Global Offensive\\csgo.exe")
        
        
        elif 'anekdot' in cmd:
            x = random.choice(jokes.jokes)
            y = ["Извините, если это было не смешно, я исправлюсь", "хахахаха... ну и умора я", "это была моя лучшая шутка"]
            z = random.choice(y)
            speak(x)
            time.sleep(1)
            speak(z)
            
        
        elif 'talk' in cmd:
            speak("Я пока что не умею разговаривать, но вскоре научусь")
        

        
        else:
            pass
    except:
        pass


    
def sendTheMessage():
    global voice
    global messageState
    if messageState == "whoState":
        message.sendWho(voice)
        speak("Что будем писать?")
        messageState = "whatState"
    elif messageState == "whatState":
        message.sendWhat(voice)
        messageState = "more"
        speak("Хотите написать что нибудь ещё?")
    elif messageState == "more":
        if voice == "да":
            messageState = "whatState"
        elif voice == "нет":
            speak("Хорошо")
            messageState = " "
        


def shutDownThisProgramAndOpenMain():
    subprocess.Popen(['python', r'F:\Jarvis\main.py'])
    os.system('cls')
    exit(0)

# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)
 
with m as source:
    r.adjust_for_ambient_noise(source)
 
speak_engine = pyttsx3.init()
 
# Только если у вас установлены голоса для синтеза речи!
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[3].id)
 
now = datetime.datetime.now()
if now.hour <= 12 and now.hour >= 6:
    speak("Доброе утро, чем могу быть полезен?")
elif now.hour >= 13 and now.hour <= 18:
    speak("Добрый день, чем могу быть полезен?")
elif now.hour >= 19 and now.hour <= 24:
    speak("Добрый вечер, чем могу быть полезен?")
elif now.hour <= 5:
    speak("Уже поздно, но я всегда готов вам помогать, чем могу быть полезен?")

while True:
    with m as source:
        audio = r.listen(source)
    callback(r, audio)
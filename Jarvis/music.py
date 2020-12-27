from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pickle
from selenium import webdriver
import requests
import time
import psutil


path = r'F:\Something\\chromedriver.exe'


def playMusic():
    global browser
    try:
        browser = webdriver.Chrome(executable_path=path)
        browser.get('https://vk.com/audios211416893')
        for cookie in pickle.load(open(r'F:\Repository\VoiceAssist\Jarvis\cookies.txt', 'rb')):
            browser.add_cookie(cookie)
        browser.get('https://vk.com/audios211416893')
        time.sleep(2)
        browser.find_element_by_class_name('audio_page__shuffle_all_button').click()
        time.sleep(2)
    except:
        print("Не получилось открыть браузер")

def offMusic():
    browser.close()

def skipSong():
    try:
        skip = browser.find_elements_by_class_name('audio_page_player_ctrl')
        skip[2].click()
    except:
        print("Не получилось скипнуть")
#Загрузка куки
def saveCookie():
    browser = webdriver.Chrome(executable_path=path)
    browser.get('https://vk.com/audios211416893')
    time.sleep(30)
    pickle.dump(browser.get_cookies(), open(r'F:\Repository\VoiceAssist\Jarvis\cookies.txt', 'wb'))
    print('Куки сохранены')



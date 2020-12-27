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



browser = webdriver.Chrome(executable_path=path)
browser.get('https://vk.com/audios211416893')
time.sleep(20)
pickle.dump(browser.get_cookies(), open(r'F:\Repository\VoiceAssist\Jarvis\session', 'wb'))
print('Куки сохранены')

#Загрузка куки

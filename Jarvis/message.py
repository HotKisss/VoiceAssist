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


path = r'F:\Something\\chromedriver.exe'

def sendMessage():
    global browser
    try:
        browser = webdriver.Chrome(executable_path=path)
        browser.get('https://vk.com/im')
    #time.sleep(30)
    #pickle.dump(browser.get_cookies(), open(r'F:\Jarvis\session', 'wb'))
    #print('Куки сохранены')
        for cookie in pickle.load(open(r'F:\Jarvis\session', 'rb')):
            browser.add_cookie(cookie)

        browser.get('https://vk.com/im')
        time.sleep(2)
    except:
        print("Не получилось открыть браузер")
def sendWho(who):
    print("asdasd")
    searchStr = browser.find_element_by_id('im_dialogs_search')
    searchStr.send_keys(who)
    time.sleep(2)
    browser.find_element_by_class_name('nim-dialog_classic').click()
def sendWhat(what):
    msgInput = browser.find_element_by_id('im_editable0')
    msgInput.send_keys(what)
    time.sleep(1)
    browser.find_element_by_class_name('im-send-btn_send').click()

#def pickDialog():

    







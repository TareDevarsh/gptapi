from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import undetected_chromedriver as uc
from gtts import gTTS
import os
from fake_useragent import UserAgent
import pyttsx3



userid = 'ENTER USER ID'
password = 'ENTER PASSWORD'

engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

# uc.TARGET_VERSION = 114
def send_and_read(inputData):
    pass
dc = DesiredCapabilities.CHROME
dc['goog:loggingPrefs'] = { 'browser':'ALL' }

ua = UserAgent()
user_agent = ua.random
print(user_agent)

option = webdriver.ChromeOptions()
# option.add_argument(f'user-agent={user_agent}')
# option.add_argument("--window-size=1920,1080")
# option.add_argument("--start-maximized")
# option.add_argument("--no-sandbox")
# option.add_argument('--disable-blink-features=AutomationControlled')
# option.add_argument("--remote-debugging-host=127.0.0.1")
# option.add_experimental_option("useAutomationExtension", False)
option.add_argument("--disable-gpu")
option.add_argument("--no-sandbox")
option.add_argument("--disable-setuid-sandbox")
# option.add_experimental_option("excludeSwitches",["enable-automation"])
# option.add_argument("--remote-debugging-port=65139")
option.add_argument('--disable-logging')
option.add_argument('--disable-extensions')
option.add_argument('--disable-infobars')
option.add_argument('--disable-blink-features=AutomationControlled')

# driver = uc.Chrome(headless=True,use_subprocess=False,options=option)
driver = webdriver.Chrome(options=option)
driver.get("https://chat.openai.com/chat")
sleep(5)
driver.execute_script('''
        for (const div of document.querySelectorAll('button')) {
            if (div.textContent.includes('Log in')) {
                div.click()
            }
        }
         ''')

sleep(5)

if "https://auth0.openai.com/u/login/identifier" in driver.current_url:
    driver.execute_script('''
        document.getElementsByClassName('input c10744244 cf50dd0ab')[0].value = "{0}";
        document.querySelectorAll('[name="action"]')[0].click();
        '''.format(userid))
    sleep(2)
    driver.execute_script('''
        document.querySelector('[id="password"]').value = "{0}";
        document.querySelectorAll('[name="action"]')[0].click();
        '''.format(password))

    sleep(5)
    driver.execute_script('''
        document.getElementsByClassName('btn relative btn-primary')[1].click()
        ''')
    print('We in Boss')
    sleep(2)
    inputData = '''
    Can you pretend that you are my AI assistant called friday? Can your first reply back be only -  "Initializing protocals. Welcome boss, what would you like me to do?"
    '''
    sleep(1)
    driver.find_element(By.ID, 'prompt-textarea').send_keys(inputData)
    sleep(1)
    driver.find_element(By.ID, 'prompt-textarea').send_keys(Keys.RETURN)
    sleep(7)
    replyLatest = driver.execute_script('''
    return document.getElementsByClassName('group w-full text-token-text-primary border-b border-black/10 dark:border-gray-900/50 bg-gray-50 dark:bg-[#444654]')[{0}].innerText
    '''.format(0)).replace('ChatGPT', '')
    print(replyLatest)
    # tts = gTTS(text=replyLatest,
    #         lang='en',
    #         slow=False)
    # tts.save("tts.mp3.mp3")
    # os.system('tts.mp3 mpg123')
    engine.say(replyLatest)
    engine.runAndWait()

    for i in range(50):
        inputData = input('--------\nSpeak now: ')
        driver.find_element(By.ID, 'prompt-textarea').send_keys(inputData)
        sleep(1)
        driver.find_element(By.ID, 'prompt-textarea').send_keys(Keys.RETURN)
        sleep(10)
        replyLatest = driver.execute_script('''
        return document.getElementsByClassName('group w-full text-token-text-primary border-b border-black/10 dark:border-gray-900/50 bg-gray-50 dark:bg-[#444654]')[{0}].innerText
        '''.format(i+1)).replace('ChatGPT', '')
        print(replyLatest)
        # tts = gTTS(text=replyLatest,
        #            lang='en',
        #             slow=False)
        # tts.save("tts.mp3")
        # os.system('tts.mp3 mpg123')
        engine.say(replyLatest)
        engine.runAndWait()




driver.quit()
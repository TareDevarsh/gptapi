from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
import socket
import threading
import os




# uc.TARGET_VERSION = 114
def send_and_read(inputData):
    pass


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', 0))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    port = s.getsockname()[1]


def open_chrome():
    url = r"https://chat.openai.com"
    chrome_path = r"/usr/bin/google-chrome"
    chrome_cmd = f"{chrome_path} --remote-debugging-port={port} --user-data-dir=remote-profile {url}"
    os.system(chrome_cmd)

chrome_thread = threading.Thread(target=open_chrome)
chrome_thread.start()

print("You need to manually complete the log-in or the human verification if required.")

while True:
    user_input = input(
        "Enter 'y' if you have completed the log-in or the human verification, or 'n' to check again: ").lower()

    if user_input == 'y':
        print("Continuing with the automation process...")
        break
    elif user_input == 'n':
        print("Waiting for you to complete the human verification...")
        time.sleep(5)  # You can adjust the waiting time as needed
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

chrome_options = webdriver.ChromeOptions()
chrome_driver_path = r"/media/dev/ubuntu/code/gptapi/chromedriver/chromedriver"
chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")
driver = webdriver.Chrome(options=chrome_options)

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
return document.getElementsByClassName('w-full text-token-text-primary')[{0}].innerText
'''.format(1)).replace('ChatGPT', '')
print(replyLatest)
os.system(f'pico2wave --lang=en-GB --wave=temp.wav "{replyLatest}"')
os.system('play temp.wav tempo 1.3')


for i in range(1,50,2):
    inputData = input('--------\nSpeak now: ')
    driver.find_element(By.ID, 'prompt-textarea').send_keys(inputData)
    sleep(1)
    driver.find_element(By.ID, 'prompt-textarea').send_keys(Keys.RETURN)
    sleep(10)
    replyLatest = driver.execute_script('''
    return document.getElementsByClassName('w-full text-token-text-primary')[{0}].innerText
    '''.format(i+2)).replace('ChatGPT', '')
    print(replyLatest)
    os.system(f'pico2wave --lang=en-GB --wave=temp.wav "{replyLatest}"')
    os.system('play temp.wav tempo 1.3')

    
driver.quit()

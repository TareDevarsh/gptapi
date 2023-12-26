
import socket
import threading
import os



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', 0))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    port = s.getsockname()[1]


def open_chrome():
    url = r"https://chat.openai.com"
    chrome_path = r"/usr/bin/firefox"
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
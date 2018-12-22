import pyperclip, time
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://www.google.co.in/search?q=")
time.sleep(10)
recent_value = ""
googurl = "https://www.google.co.in/search?q="
while True:
    tmp_value = pyperclip.paste()
    if tmp_value == "exit":
        break
    if tmp_value != recent_value:
        recent_value = tmp_value
        print(googurl+tmp_value)
        browser.get(googurl+tmp_value)
    time.sleep(0.1)


browser.quit()

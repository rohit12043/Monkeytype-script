from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("https://monkeytype.com")
time.sleep(3) 

try: 
    while True:
        word = driver.find_element(By.CSS_SELECTOR, ".word.active")
        current = word.text

        text_input = driver.find_element(By.ID, "wordsInput")
        text_input.clear()

        text_input.send_keys(current + " ")
except Exception as e:
    print("Typing finished: ")

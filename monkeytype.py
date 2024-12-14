from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import keyboard
import random

driver = webdriver.Firefox()

driver.get("https://monkeytype.com")
time.sleep(3) 
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="active acceptAll"]'))).click()

time_config_options = [15, 30, 60, 120]
print(f"Available time configurations: {time_config_options}")
user_input = int(input("Enter your desired time configuration (15, 30, 60, 120): "))

if user_input not in time_config_options:
    print("Invalid selection. Exiting.")
    driver.quit()
else:
    try:
        button_xpath = f'//button[@class="textButton" and @timeconfig="{user_input}"]'
        time_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, button_xpath))
        )
        time_button.click()
        print(f"{user_input}-second time configuration selected.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Driver is ready.")

try:
    while True:
        if keyboard.is_pressed("q"):
            print("Q key pressed. Stopping script.")
            break
        
        word = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".word.active"))
        )
        text_input = driver.find_element(By.ID, "wordsInput")
        time.sleep(random.uniform(0.5, 0.65))
        text_input.send_keys(word.text + " ")  
except Exception as e:
    print("Typing finished.")
finally:
    print("Driver is still running. Press 'q' to quit.")
    while not keyboard.is_pressed("q"):
        pass
    driver.quit() 

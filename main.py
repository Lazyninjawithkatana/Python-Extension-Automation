from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
from time import sleep

gecko_path = '/home/noname/Desktop/okx/geckodriver'
firefox_profile = '/home/noname/.mozilla/firefox/2ykusf7u.default-esr'

options = Options()
options.set_preference('xpinstall.signatures.required', False)
options.set_preference('extensions.autoDisableScopes', 0)
options.add_argument(f'--profile={firefox_profile}')

service = Service(gecko_path)
driver = webdriver.Firefox(service=service, options=options)
wait = WebDriverWait(driver, 5)

target_url = 'moz-extension://c936d1e2-217f-43aa-b48e-ba18e5fb01ba/index.html'
driver.get(target_url)

sleep(4) 

def login_attempt():
    with open('cleaned.txt', 'r') as words:
        seed_phrases = words.read().replace('\n', '').split(',')

    try:
        input_fields = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'mnemonic-words-inputs__container__input'))
        )
    except Exception as a:
        print(f'[!] Error finding inputs: {a}')
        return

    while True:

        chosen_words = random.sample(seed_phrases, 12)

        for field, word in zip(input_fields, chosen_words):
            field.clear()
            field.send_keys(word)

        try:
            button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'okui-btn')]"))
            )
        except Exception as e:
            print(f'[!] Error finding button: {e}')
            continue

        if button.is_enabled():
            print('[+] The correct option has been found!')

            with open('successful_attempts_okx_1.txt', 'a', encoding='utf-8') as file:
                file.write(' '.join(chosen_words) + '\n')
                file.flush()

        else:
            print('[!] Wrong words - Retrying...')
            for field in input_fields:
                field.clear()

login_attempt()

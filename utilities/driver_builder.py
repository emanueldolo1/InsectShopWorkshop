from utilities import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import sys


def build_driver():
    browser = config.BROWSER

    if browser == "chrome":
        chrome_options = Options()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()

    elif browser == "chrome-headless":
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)

    elif browser == "firefox":
        driver = webdriver.Firefox(log_path=os.devnull)

    else:
        sys.exit("Browser not supported!")

    return driver

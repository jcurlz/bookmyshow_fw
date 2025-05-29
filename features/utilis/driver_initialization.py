#driver_initialization.py
import undetected_chromedriver as uc
from selenium import webdriver

def initialize_driver():
    option = uc.ChromeOptions()
    # options.headless = True
    option.add_argument("--incognito")
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-gpu")
    option.add_argument("--disable-extensions")
    initilaized_driver = uc.Chrome(version_main=136, options=option)
    print("[DEBUG] Driver initialized successfully")
    return initilaized_driver

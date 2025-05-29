#base_methods.py
import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class BaseMethods():
    BASE_URL = 'https://in.bookmyshow.com/'
    def __init__(self, env_driver):
        self.shared_driver = env_driver
        self.wait = WebDriverWait(self.shared_driver, 15)
        
    def open_url(self):
        self.shared_driver.get(self.BASE_URL)
        logging.info("✅ Opening URL...")
        time.sleep(2)

    def true_or_false(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            time.sleep(1)
            if element.is_displayed():
                logging.info("✅ Element is visible: ")
                return True
            else:
                logging.error("❌ Element is present but not visible")
                return False
        except TimeoutException:
            logging.error("❌ Timeout: Element not found")
            return False
        except Exception as e:
            logging.error("❌ Unexpected error checking visibility: {locator}, Exception: {e}")
            return False

    def check_element_presence(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            logging.info("✅ Element found: {locator}")
            return element
        except Exception as e:
            logging.error("❌ Element not found: {locator} Exception: {e}")
            return None

    def click_on_element(self, locator):
        self.wait.until(EC.element_to_be_clickable((locator))).click()
        logging.info("✅ Element clicked: %s", locator)
        time.sleep(2)

    def clear_the_textbox(self, locator):
        element = self.wait.until(EC.element_to_be_clickable((locator)))        
        element.clear()
        logging.info("✅ Element cleared: %s", locator)
        time.sleep(2)

    def enter_text(self, locator, text):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).send_keys(text)
            logging.info(f"✅ {text} passed")
        except TimeoutException:
            logging.info("Timeout: Element not found")
        time.sleep(2)

    def get_dropdown_list(self, locator):
        try:
            # self.check_element_presence(locator)
            elements = self.shared_driver.find_elements(*locator)
            actual_list = []
            for el in elements:
                logging.info(f" Before stripping el.text {el.text}")
                text = el.text.strip().lower()
                logging.info(f" After stripping text: {text} ")
                logging.info(f" After replacing empty spaces text: {re.sub(r"[\n]", ",", text)} ")
                logging.info(f" After splitting them based on (,): {re.sub(r"[\n]", ",", text).split(",")} ")
                text = [text.strip().lower() for text in re.sub(r"[\n]", ",", text).split(",") if text]

                actual_list.extend(text)
            logging.info(f"DEBUG >> Actual Words list: {actual_list}")
            return actual_list
        except TimeoutException:
            logging.error("❌ Suggestions not found in time")
            return []

    def locate_the_dropdown_suggestion_and_click(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator)).click()
            logging.info(f"✅ Dropdown suggestion option selected")
        except Exception as e:
            logging.error(f"❌ <DEBUG> Failed to find element: {e}")

   

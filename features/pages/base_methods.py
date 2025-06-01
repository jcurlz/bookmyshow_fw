#base_methods.py
import re
import time
from argparse import Action

from selenium.webdriver import ActionChains
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
        self.action = ActionChains(self.shared_driver)

    def open_url(self, url):
        self.shared_driver.get(url)
        logging.info("✅ Opening URL...")
        time.sleep(0.5)

    def verify_the_url(self, exp_url):
        logging.info("🔍 Asserting the Current URL...")
        current_url = self.shared_driver.current_url
        if current_url == exp_url:
            logging.info(f"✅ 🌐 Successfully navigated to {exp_url} : {current_url}")
        else:
            logging.error(f"❌ 🌐  Navigation failed. Expected: {exp_url}, Got: {current_url}")

    def return_the_url(self):
        logging.info("🔍 Asserting the Current URL...")

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
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.action.move_to_element(element).perform()
            time.sleep(1.5)
            element.click()
            logging.info("✅ Element found & clicked")
            return self.shared_driver.current_url
        except Exception as e:
            logging.error(f"❌ Element not found: {locator} Exception: {e}")
            return None

    def clear_the_textbox(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
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

    def assert_the_options(self, locator, expected_options):
        # Step 1: Strip the special charac:
        split_data = expected_options.split("&")
        logging.info(f"DEBUG >> After split on &: {split_data}")

        # Step 2: Clean each part: strip spaces, remove inner spaces, lowercase
        exp_list = [e.strip().replace(" ", "").lower() for e in split_data if e.strip()]
        logging.info(f"DEBUG >> Final cleaned list: {exp_list}")

        actual_list= []
        element = self.wait.until(EC.presence_of_all_elements_located(locator))
        for el in element:
            logging.info(f" Before stripping el.text {el.text}")
            text = el.text.strip().lower().replace(" ","")
            logging.info(f" After stripping text and replacing empty space: {text} ")
            e_list = [e.strip() for e in re.sub(r"[\W]"," ",text).split() if e]
            logging.info(f" After loop via for-each : {e_list} ")
            actual_list.extend(e_list)
        logging.info(f"Final List: {actual_list} ")
        for index, (act,exp) in enumerate(zip(actual_list,exp_list), start = 1):
            if act == exp:
                logging.info(f"✅ Match found {index}: '{exp}' in {act}")
            else:
                logging.error(f"❌ '{exp}' not found in actual suggestions: {act}")
                assert False, f"❌ Expected word '{exp}' not found in actual suggestions"


    def assert_the_text(self, locator, expected_text):
        expected_text = expected_text.strip().lower().replace('"', '')
        expected_text = re.sub(r"[\s'-]","",expected_text).split()
        logging.info(f"Date Range Expected : {expected_text}")
        actual_text = None
        try:
            time.sleep(1)
            element = self.wait.until(EC.presence_of_element_located(locator))
            actual_text = element.text.strip().lower()
            actual_text = [e.strip() for e in re.sub(r"[\s'-]", "",actual_text).split() if e]
            logging.info(f"Actual Date Range {actual_text}")
        except Exception as e:
            logging.error(f"<UNK> <DEBUG> Failed to find element: {e}")
        logging.info(f"{actual_text} == {expected_text}")
        assert actual_text == expected_text, f"Expected {expected_text} but got {actual_text}"
        time.sleep(2)


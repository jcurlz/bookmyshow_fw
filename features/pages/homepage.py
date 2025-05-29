# homepage.py
import time
import re

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.ui import WebDriverWait


class HomePage():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # HOME PAGE Object
    logo_ele = (By.CLASS_NAME, 'gNQLww')
    homepg_loc_ele = (By.ID, 'common-header-region')
    homepg_loc_box_search_field = (By.XPATH, '//input[@type="text"]')
    homepg_loc_box_chennai_sugg = (By.XPATH, "//span[contains(@class,'bwc__sc-ttnkwg-14 cXklvo')  and contains(., 'Chennai')]")
    act_loc_suggestions_list = (By.XPATH, '//*[@id="modal-root"]/div/div/div/div[1]/div[2]/div/ul') #//*[@class="bwc__sc-1iyhybo-11 hCnsML"]')

    #CONSTANTS
    HOMEPG_CHENNAI = "https://in.bookmyshow.com/explore/home/chennai"


    def __init__(self, base_methods):
        self.base = base_methods
        self.wait = WebDriverWait(self.base.shared_driver, 15)
        
    def click_on_location_box(self, locator):
        element = self.base.check_element_presence(locator)
        if element:
            self.base.click_on_element(element)
            logging.info("✅ Location box is clicked")
        else:
            logging.error("❌ Failed to find location box to click")


    def assert_dropdown_list(self, exp_loc_suggestions):
        expected_words = []
        #cleaned_input = exp_loc_suggestions.replace("&", ",")
        #cleaned_input = re.sub(r"[&/|@]", ",", exp_loc_suggestions)
        # logging.info(f" Before processing exp: {cleaned_input} ")

        # Split cleaned input by comma and strip/lowercase each word
        # Clean data and split
        logging.info(f"DEBUG >> Expected Words (input): {exp_loc_suggestions}")
        #Joined is not required here as it is effective for iteratable elements
        joined_data = "".join(exp_loc_suggestions)
        logging.info(f"DEBUG >> Expected Words (joined_data): {joined_data}")

        clean_data = re.sub("[&]",",",joined_data)
        logging.info(f"DEBUG >> Expected Words (clean_data): {clean_data}")

        expected_words = [word.strip().lower() for word in clean_data.split(",") if word]
        logging.info(f"DEBUG >> Expected Words: {expected_words}")

        # Get actual suggestions as list of words
        actual_list = self.base.get_dropdown_list(self.act_loc_suggestions_list)

        for exp_word in expected_words:
            if exp_word in actual_list:
                logging.info(f"✅ Match found: '{exp_word}' in {actual_list}")
            else:
                logging.error(f"❌ '{exp_word}' not found in actual suggestions: {actual_list}")
                assert False, f"❌ Expected word '{exp_word}' not found in actual suggestions"

    def click_enter_and_choose_desired_option(self, suggestion):
        logging.info(f"🔍 Searching for the location box.....")
        self.base.click_on_element(self.homepg_loc_box_search_field)
        time.sleep(2)
        logging.info("🧹 Clearing the input textbox in the location field...")
        self.base.clear_the_textbox(self.homepg_loc_box_search_field)
        time.sleep(2)
        logging.info("📝 Entering the search term in the location box...")
        self.base.enter_text(self.homepg_loc_box_search_field, suggestion)
        time.sleep(2)
        logging.info("🔍 Searching for the desired suggestion in the dropdown...")
        self.base.locate_the_dropdown_suggestion_and_click(self.homepg_loc_box_chennai_sugg)
        time.sleep(10)

    def verify_the_url(self):
        logging.info("🔍 Asserting the Current URL...")
        current_url = self.base.shared_driver.current_url
        assert self.HOMEPG_CHENNAI == current_url, f"❌ Expected URL: {self.HOMEPG_CHENNAI}, but got: {current_url}"
        logging.info("✅ Asserted the Current URL...")
#playpage.py
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class PlayPage:

    logging.basicConfig(filename='playpage.log', level=logging.DEBUG)

    # CONSTANTS
    CHENNAI_URL ="https://in.bookmyshow.com/explore/home/chennai"
    PLAYS_URL = "https://in.bookmyshow.com/explore/plays-chennai"

    #Objects
    date_filter = (By.XPATH, "//div[contains(@class,'alhxg')  and text()='Date']")
    date_filter_components = (By.XPATH, "//div[contains(@class,'jcjdBd')]")
    date_range_checkbox = (By.XPATH, "//div[@class='sc-1w4xxzu-1 ielWHn']")
    date_range_right_arrow = (By.XPATH, "//div[@class='sc-8opt4a-1 epDIPD'][2]")
    date_range_month = (By.XPATH, "//div[@class='sc-8opt4a-4 irsvzW']")
    date_range_dec = (By.XPATH, "//div[@class='sc-8opt4a-4 irsvzW' and contains(.,'December 2025')]")
    date_range_apply_button = (By.XPATH, "//div[contains(@class,'sc-7o7nez-0 jOzSQH') and text()='Apply']")

    date_range_confirmation = (By.CSS_SELECTOR, ".sc-1w4xxzu-2")
    lang_filter = (By.XPATH, "//div[contains(@class,'dksMXb') and text()='Language' and text()='English'] ")
    lang_filter_components = (By.XPATH, "//div[div[text()='Language']]/following-sibling::div[contains(@class,'jcjdBd')]")


    def __init__(self, base_methods, homepage):
        self.base = base_methods
        self.playpg_from_homepg = homepage
        self.wait = WebDriverWait(self.base.shared_driver, 15)


    def verify_the_url(self, locator):
        self.base.op(locator)


    def element_click(self, locator):
        element = self.base.check_element_presence(locator)
        if element.is_enabled():
           logging.info(f"DEBUG >> Date Filter enabled by default")
        if not element.is_enabled():
            self.base.click_on_element(locator)
            logging.info(f"DEBUG >> Date Filter enabled by click")


    def verify_the_filter_components(self, locator, exp_options):
        self.base.get_dropdown_list(locator, exp_options)

    def click_right_arrow(self, month_year):
        logging.info(f"DEBUG >> Date_range_dec Right arrow click scenario....")
        while True:
            current = self.wait.until(EC.visibility_of_element_located(self.date_range_month))
            current_text = current.text.strip()
            logging.info(f"DEBUG >> Current text: {current_text}")
            attempt = 1
            logging.info(f"Attempt : {attempt}")
            try:
                if current_text == month_year:
                    logging.info(f"DEBUG >> Match found: {current_text} == {month_year}")
                    break

                attempt+=1
                logging.info("DEBUG >> Clicking right arrow to find expected text...")
                self.wait.until(EC.element_to_be_clickable(self.date_range_right_arrow)).click()
            except Exception as e:
                logging.info(f"DEBUG >> Exception: {e}")


    def click_date(self, day, month):
        logging.info(f"DEBUG >> Click date {day} {month}")
        try:
            day_locator = self.wait.until(EC.presence_of_element_located((By.XPATH, f"//div[text()='{day}' and contains(@title,'{month}')]")))
            self.wait.until(EC.element_to_be_clickable(day_locator))
            logging.info(f"✅ Element found for {day}, {month}")
            self.base.click_on_element(day_locator)
        except Exception as e:
            logging.info(f"DEBUG >> Exception in click_date: {e}")
        time.sleep(2)


    def assert_date_confirmation(self, expected_date_range):
        self.base.assert_the_text(self.date_range_confirmation, expected_date_range)
        logging.info(f"DEBUG >> Date range assertion done")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class EventsPage:
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    #Event Page Locators
    price_filter = (By.XPATH,"//*[contains(@class,'sc-133848s-1 sc-1y4pbdw-9 bSUVYF cHFkHE')]/following::*[text()='Price']")
    price_filter_component = (By.XPATH, "//*[div[div[contains(text(),'Price')]]]//*[contains(@class,'sc-133848s-2 sc-1y4pbdw-11 ccqrhI jcjdBd')]")
    price_exp_range = (By.XPATH, "//*[contains(@class,'sc-7o7nez-0 hRJgHk') and contains(text(),'0 - 500')]")
    card_by_title = (By.XPATH, "//*[contains(@class,'sc-7o7nez-0 elfplV') and contains(text(),'Rambo Circus - Chennai')]")
    card_3 = (By.XPATH ,"(//*[contains(@class,'sc-133848s-11 sc-1ljcxl3-1 ctsexn uPavs')][3]//*[contains(@class,'sc-7o7nez-0 elfplV')])[1]")
    book_now_btn = (By.XPATH,"//*[text()='Book Now']")
    select_date = (By.XPATH,"(//*[contains(@class,'sc-w5ft3r-0 ecpmRI')]//child::*[contains(@class,'sc-12lbmff-0 fGubkX')])[2]")
    select_time = (By.XPATH,"(//*[contains(@class,'sc-humnht-0 aQQDP')]//child::*[contains(@class,'sc-12lbmff-0 fGubkX')])[1]")
    proceed_btn = (By.XPATH,"//*[contains(@class,'sc-zgl7vj-8 hpVUcY')]")
    add_tickets_btn = (By.XPATH,"//*[contains(@class,'sc-q3g70i-12 exCdIS')]")
    add_3_tickets = (By.XPATH,"//*[contains(@class,'sc-q3g70i-13 jSWPnt')][2]")


    #CONSTANTS
    EVENTSPG_CHENNAI = "https://in.bookmyshow.com/explore/events-chennai"

    def __init__(self, base_methods):
        self.base = base_methods
        self.wait = WebDriverWait(self.base.shared_driver, 15)


    def click_seats(self, expected_seat):
        try:
            seat_loc = (By.XPATH, f"//*[contains(@class,'sc-1c515um-2 ctqvKA')]/child::*[contains(text(),'{expected_seat}')]")
            select_set_count = self.wait.until(
                EC.presence_of_element_located(seat_loc))
            if select_set_count:
                logging.info(f"Element located")
            else:
                pass
            self.base.click_on_element(select_set_count)
            logging.info(f"Element clicked")
        except Exception as e:
            logging.error(f"Element Not Located {e}")


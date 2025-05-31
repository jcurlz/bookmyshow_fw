from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging,time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)
driver.get("https://in.bookmyshow.com/explore/plays-chennai")
driver.maximize_window()
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-1w4xxzu-1 ielWHn']"))).click()
time.sleep(2)
date_range_right_arrow = (By.XPATH, "//div[@class='sc-8opt4a-1 epDIPD'][2]")
date_range_month = (By.XPATH, "//div[@class='sc-8opt4a-4 irsvzW']")
date_range_dec = (By.XPATH, "//div[@class='sc-8opt4a-4 irsvzW' and contains(.,'December 2025'')]")
expected_text = "December 2025"

logging.info(f"DEBUG >> date_range_dec locator: {date_range_dec}")
while True:
    current = wait.until(EC.presence_of_element_located((date_range_month)))
    current_text = current.text.strip()
    logging.info(f"DEBUG >> Current text: {current_text}")
    attempt = 1
    try:
        if current_text == expected_text:
            logging.info(f"DEBUG >> Match found: {current_text} == {expected_text}")
            time.sleep(2)
            break
    except:
        logging.info(f"Attempt {attempt} - No such element")
        attempt += 1
        pass
    logging.info("DEBUG >> Clicking right arrow to find expected text...")
    wait.until(EC.element_to_be_clickable(date_range_right_arrow)).click()
    time.sleep(1)
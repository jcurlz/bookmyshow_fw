from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging,time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)
action = ActionChains(driver)
driver.get("https://in.bookmyshow.com/explore/plays-chennai?daygroups=custom:20251225-20251230")
date_range_confirmation = (By.XPATH,"//div[contains(@class,'sc-1w4xxzu-2 jIwerK')]")
driver.maximize_window()
time.sleep(1)

expected_text = "25' Dec 25 - 30' Dec 25"
expected_text = expected_text.strip().lower()
expected_text = expected_text.split()
logging.info(f"{expected_text}")
actual_text = None
try:
    element = wait.until(EC.presence_of_element_located(date_range_confirmation))
    actual_text = element.text.strip().lower()
    actual_text = actual_text.split()
except Exception as e:
    logging.error(f"<UNK> <DEBUG> Failed to find element: {e}")
logging.info(f"{actual_text} == {expected_text}")
assert {actual_text} == {expected_text}, f"Expected {expected_text} but got {actual_text}"

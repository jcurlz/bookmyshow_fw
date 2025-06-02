import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging,time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

option = uc.ChromeOptions()
option.add_argument('--incognito')
driver = uc.Chrome(version_main=136, options=option)
wait = WebDriverWait(driver, 15)
action = ActionChains(driver)
driver.maximize_window()

driver.get("https://in.bookmyshow.com/explore/plays-chennai")
date_range_checkbox = (By.XPATH, "//div[@class='sc-1w4xxzu-1 ielWHn']")
date_range_apply_button = (By.XPATH, "//div[contains(@class,'sc-7o7nez-0 jOzSQH')]")

#To click on the Date Range checkbox
wait.until(EC.presence_of_element_located(date_range_checkbox)).click()
print("Date Range clicked")
time.sleep(1)

#To select the Start date
start_dt = driver.find_element(By.XPATH, "//*[contains(@title,'Jun 02')]")
action.move_to_element(start_dt).perform()
print("Action hover (start date) performed")
time.sleep(3)
action.move_to_element(start_dt).click().perform()
time.sleep(3)
print("Action click (start date)  done")

#To select the End date
start_dt = driver.find_element(By.XPATH, "//*[contains(@title,'Jun 22')]")
action.move_to_element(start_dt).perform()
print("Action hover (end date) performed")
time.sleep(3)
action.move_to_element(start_dt).click().perform()
print("Action click (end date) done")
time.sleep(3)

#To click on the Apply button
wait.until(EC.element_to_be_clickable(date_range_apply_button)).click()
print("Action click (Apply button) done")
time.sleep(5)
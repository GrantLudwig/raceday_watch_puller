from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
try:
    driver.get("https://raceday.watch/#sessions")
    assert "RaceDay.watch" in driver.title
    WebDriverWait(driver, 100).until(
        lambda driver: driver.find_element(By.CLASS_NAME, "qx-session-item"))
    elem = driver.find_elements(By.CLASS_NAME, "qx-session-item")
    print("Print", elem)
    elem.clear()
except Exception as e:
    print("Exception occured")
    print(e)

driver.close()
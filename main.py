import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

def print_event_info(session_info):
    for info in session_info:
        print(info.text)
    print()

driver = webdriver.Chrome()
actions = ActionChains(driver)
try:
    driver.get("https://raceday.watch/#sessions")
    assert "RaceDay.watch" in driver.title
    WebDriverWait(driver, 100).until(
        lambda driver: driver.find_element(By.CLASS_NAME, "qx-session-item"))

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    events = driver.find_elements(By.CLASS_NAME, "qx-session-item")
    races_to_track = []
    for session in events:
        actions.move_to_element(session).perform()
        session_info = session.find_elements(By.XPATH, "./*")
        if len(session_info) > 3:
            raise Exception("Website changed, need to update code")
        
        event_running, race_info, track_name = session_info
        if bool(re.search("Spa-Francorchamps", track_name.text, flags=re.IGNORECASE)):
            races_to_track.append(session)
            print_event_info(session_info)
        elif bool(re.search("Nürburgring Nordschleife", track_name.text, flags=re.IGNORECASE)):
            races_to_track.append(session)
            print_event_info(session_info)

    print("Number Races:", len(races_to_track))
    events.clear()

except Exception as e:
    print("Exception occured")
    print(e)

driver.close()
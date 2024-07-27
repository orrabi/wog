from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import ChromiumOptions
import sys
import time

def test_scores_service(url):

    chrome_options = ChromiumOptions()
    service = Service(ChromeDriverManager().install(), options=chrome_options)

    driver = webdriver.Chrome(service=service)

    driver.get("http://localhost:5001/")
    score_element = driver.find_element(By.ID, "score")
    if not score_element:
        print("No element was found!")
        return False
    score = int(score_element.text)
    if not score:
        print("Score was not found!")
        return False
    if 1 <= score <= 1000:
        return True
    else:
        return False


def main_function():
    app_url = "http://localhost:5001/"
    result = test_scores_service(app_url)
    if result:
        return sys.exit(0)
    else:
        return sys.exit(-1)


main_function()
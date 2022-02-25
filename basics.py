from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/Applications/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("http://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")

driver.implicitly_wait(3)  # could have used time.sleep(3)

downloadButton = driver.find_element_by_id("downloadButton")
downloadButton.click()

progressElement = driver.find_element_by_class_name("progress-label")
print(progressElement.text)

WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),
        'Complete!'
    )
)

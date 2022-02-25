from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "/Applications/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get('http://demo.seleniumeasy.com/basic-first-form-demo.html')
driver.implicitly_wait(5)
try:
    noButton = driver.find_element_by_class_name('at-cm-no-button')
    noButton.click()
except:
    print('No element with class name. Skipping...')

sum1 = driver.find_element_by_id('sum1')
sum2 = driver.find_element_by_id('sum2')

sum1.send_keys(10)
sum2.send_keys(Keys.NUMPAD2, Keys.NUMPAD0)  # 20

submitButton = driver.find_element_by_css_selector(
    'button[onclick="return total()"]')

submitButton.click()

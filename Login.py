from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

username = 'Admin'
password = 'admin123'

driver.find_element(By.NAME, 'username').send_keys(username)
driver.find_element(By.NAME, 'password').send_keys(password)
driver.find_element(By.CLASS_NAME, 'oxd-button oxd-button--medium oxd-button--main orangehrm-login-button').click()

driver.get_screenshot_as_file('Login success.png')
driver.quit()
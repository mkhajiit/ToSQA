from selenium.webdriver.common.by import By

def login(driver):
  username_input = driver.find_element(By.CSS_SELECTOR,'[data-test = "username"]')
  username_input.send_keys("wrongusername")

  password_input = driver.find_element(By.CSS_SELECTOR, '[data-test = "password"]')
  password_input.send_keys("wrongpassword")

  login_button = driver.find_element(By.CSS_SELECTOR,'[data-test = "login-button"]')
  login_button.click()
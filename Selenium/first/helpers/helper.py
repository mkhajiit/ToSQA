from selenium.webdriver.common.by import By

def login(driver,username,password):
  username_input = driver.find_element(By.CSS_SELECTOR,'[data-test = "username"]')
  username_input.send_keys(username)

  password_input = driver.find_element(By.CSS_SELECTOR, '[data-test = "password"]')
  password_input.send_keys(password)

  login_button = driver.find_element(By.CSS_SELECTOR,'[data-test = "login-button"]')
  login_button.click()
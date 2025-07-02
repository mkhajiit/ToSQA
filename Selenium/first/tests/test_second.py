from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 잘못된 입력시 에러메시지 출력 여부 확인 테스트
def test_login_error():
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

  driver.get("https://www.saucedemo.com/")

  username_input = driver.find_element(By.CSS_SELECTOR,'[data-test = "username"]')
  username_input.send_keys("wrongusername")

  password_input = driver.find_element(By.CSS_SELECTOR, '[data-test = "password"]')
  password_input.send_keys("wrongpassword")

  login_button = driver.find_element(By.CSS_SELECTOR,'[data-test = "login-button"]')
  login_button.click()

  error_text = driver.find_element(By.CLASS_NAME, "error-message-container").text
  assert "Epic sadface" in error_text

  driver.quit()
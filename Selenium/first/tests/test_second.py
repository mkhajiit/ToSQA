import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  yield driver  # 이 시점 이전까지는 테스트 실행, Pytest가 yield 기준으로 테스트 전후 작업을 자동으로 처리해줌
  driver.quit() # 테스트 끝나면 브라우저 종료

# 잘못된 입력시 에러메시지 출력 여부 확인 테스트
def test_login_error(driver):

  driver.get("https://www.saucedemo.com/")
  wait = WebDriverWait(driver,10)

  username_input = driver.find_element(By.CSS_SELECTOR,'[data-test = "username"]')
  username_input.send_keys("wrongusername")

  password_input = driver.find_element(By.CSS_SELECTOR, '[data-test = "password"]')
  password_input.send_keys("wrongpassword")

  login_button = driver.find_element(By.CSS_SELECTOR,'[data-test = "login-button"]')
  login_button.click()

  error_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"error-message-container")))
  assert "Epic sadface" in error_box.text
import pytest
from helpers.helper import login
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
  options = Options()
  options.add_argument("--headless")  # headless 모드

  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
  driver.get("https://www.saucedemo.com/")
  yield driver  # 이 시점 이전까지는 테스트 실행, Pytest가 yield 기준으로 테스트 전후 작업을 자동으로 처리해줌
  driver.quit() # 테스트 끝나면 브라우저 종료

# 잘못된 입력시 에러메시지 출력 여부 확인 테스트
def test_login_error(driver):

  wait = WebDriverWait(driver,10)

  login(driver,"differentname","differentpassword")

  error_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"error-message-container")))
  assert "Epic sadface" in error_box.text

# 정확한 입력 테스트
def test_login_success(driver):

  wait = WebDriverWait(driver,10)

  login(driver,"standard_user","secret_sauce")

  inventory = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="inventory-container"]')))

  assert inventory is not None
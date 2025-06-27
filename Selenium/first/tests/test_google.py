from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_google_title():
    # Chrome 브라우저 자동 설정
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver.get("https://www.google.com")

    # 타이틀에 'Google'이 포함되어야 한다
    assert "Google" in driver.title

    driver.quit()
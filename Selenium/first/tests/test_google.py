from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_google_title():
    # Chrome 브라우저 자동 설정
    # 시스템에 크롬 드라이버가 없다면 자동 설치해 경로설정
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # 구글 웹사이트를 엽니다
    driver.get("https://www.google.com")

    # 타이틀 태그에 'Google'이 포함되어야 한다
    assert "Google" in driver.title

    # 브라우저를 닫고 WebDriver 프로세스를 종료
    driver.quit()
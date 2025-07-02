# 구글은 봇을 감지해서 막기 때문에 테스트 사이트를 사용해야함

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.google.com")

search_box = driver.find_element(By.CLASS_NAME,"gLFyf")
search_box.send_keys("파이썬")
search_box.submit() # Enter 입력

time.sleep(3)

# 결과 중 첫 번째 검색 결과 링크의 텍스트 출력
first_result = driver.find_element(By.CSS_SELECTOR,"h3")
print("첫 번째 검색 결과:",first_result)
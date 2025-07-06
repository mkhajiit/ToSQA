# 테스트 후 에러가 발생했을때 스크린샷을 남기도록 하는 훅 함수
import os
import pytest
import logging
from datetime import datetime

# 스크린샷, 로그 저장 폴더 생성
os.makedirs("screenshots", exist_ok=True)
os.makedirs("log", exist_ok=True)

now = datetime.now().strftime("%Y%m%d_%H%M%S") # 지금 시간을 변수로 넣어서 설정함
# 로거 설정
logging.basicConfig(
    filename= f'log/test_{now}.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8' # 로그 저장시 한글 깨지는 걸 방지함
)

# 훅 함수에 추가 옵션을 주거나 명시적으로 표시할 때 쓴다.
# hookwrapper=True → 훅 함수가 내부에서 yield를 써서 pytest 실행 흐름을 감쌀 때 필요하다.
# tryfirst=True → 여러 훅 함수 중 먼저 실행하라고 우선순위를 지정할 때 쓴다.

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
# 테스트 함수가 실행되고 결과를 만드는 시점에 호출되는 hook 함수
# item 은 현재 테스트 함수에 대한 정보를 담고 있는 객체
def pytest_runtest_makereport(item, call):
    outcome = yield # pytest가 테스트 실행을 먼저 하게 하고 결과를 받아옴
    rep = outcome.get_result() # 실제 테스트 실행 결과

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            # driver 객체가 name 속성을 가지고 있으면 그 값을 꺼내고, 없으면 "unknown" 문자열을 기본값으로 사용
            browser_name = getattr(driver, "browser_name", "unknown")
            filename = f"screenshots/{item.name}_{browser_name}.png"
            driver.save_screenshot(filename)
            print(f"스크린샷 저장됨: {filename}")
            logging.error(f"테스트 실패: {item.nodeid}") # 어떤 테스트가 실패했는지
            logging.error(f"실패 메시지: {rep.longrepr}") # AssertionError 메시지, 트레이스백(stack trace) 전체
        else:
            logging.error(f"테스트 '{item.name}' 실패! WebDriver 인스턴스를 찾을 수 없음.")

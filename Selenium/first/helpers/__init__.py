# __init__.py가 왜 필요한가?
# 파이썬은 폴더에 __init__.py 파일이 있어야 **그 폴더를 패키지(모듈 집합)**로 인식합니다.
# tests 폴더에 __init__.py가 없으면, 파이썬이 tests를 패키지로 인식하지 못해 상대/절대 import가 꼬일 수 있어요.
# 그래서 tests에 __init__.py를 넣으면,
# from helpers.helper import login 같은 절대 경로나
# from ..helpers.helper import login 같은 상대 경로 임포트가 정상 작동합니다.



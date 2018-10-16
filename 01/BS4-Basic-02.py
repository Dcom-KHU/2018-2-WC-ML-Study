# BeautifulSoup 모듈과 requests 모듈의 삽입
from bs4 import BeautifulSoup
import requests

# requests.get을 이용하여 response 객체를 반환 받는다.
url = "http://example.com"
resObj = requests.get(url)

# response 객체의 text 속성을 추출, BeautifulSoup 객체를 반환 받는다.
soupObj = BeautifulSoup(resObj.text, 'html.parser')

# css 선택자 입력 후 출력하는 모습
print(list(map(lambda x: x.text, soupObj.select('h1'))))
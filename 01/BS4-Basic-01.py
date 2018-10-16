# 라이브러리를 읽어 들인다.
from bs4 import BeautifulSoup

# 분석하고 싶은 HTML이라고 가정하자.
html = """
<h1>안녕안녕</h1>
<h2>반가웡</h2>
<h2>환영행</h2>
"""

# 그리고 BeautifulSoup 모듈 이용, BeautifulSoup 객체를 만들고 
soupObj = BeautifulSoup(html, "html.parser")

# css의 선택자를 이용하여 원하는 요소를 추출할 수 있다!
# list로 반환되는 요소는 bs4.element.tag로 string으로 형 변환 해 주어야 한다.
# 문자열 슬라이스는 같이 따라온 필요없는 태그를 제거 하기 위해 사용했다.
list_var = list(map(lambda x: x.text, soupObj.select("h2")))
print(list_var)
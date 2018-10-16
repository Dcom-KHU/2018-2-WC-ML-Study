# BeautifulSoup 모듈과 requests 모듈의 삽입
from bs4 import BeautifulSoup
import requests

# 동네 이름을 입력 받고, url에 넣어 준다
place = input("어디 동네의 날씨가 궁금하신가요? : ")
url = "http://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=" + place + " 날씨"

resObj = requests.get(url)

# 그리고 BeautifulSoup 모듈 이용, BeautifulSoup 객체를 만들고
soupObj = BeautifulSoup(resObj.text, "html.parser")

# select 함수를 통해 css의 선택자를 이용하여 원하는 요소를 추출할 수 있다!
# list로 반환되는 요소는 bs4.element.tag로 내용물에 접근 하기 위해서는...
# text 속성을 이용하여 추출 하면 된다.
# list_var에서 반환 받은 리스트는 0번째는 지금 온도, 1~2번째는 내일 최저 최고 온도, 3~4번째는 모레 최저 최고 온도이다.
todaytemp_var = list(map(lambda x: x.text+'˚', soupObj.select("span.todaytemp")))
min_str = soupObj.select_one("span.min").getText()
max_str = soupObj.select_one("span.max").getText()

print("현재 기온은 {} 입니다.".format(todaytemp_var[0]))
print("오늘 최저/최고 기온 {}/{}".format(min_str,max_str))
print("내일 최저/최고 기온 {}/{}".format(todaytemp_var[1],todaytemp_var[2]))
print("모레 최저/최고 기온 {}/{}".format(todaytemp_var[3],todaytemp_var[4]))
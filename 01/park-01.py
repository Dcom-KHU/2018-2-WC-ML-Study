import requests
from bs4 import BeautifulSoup

class Everytime():
    def __init__(self, userid, password):
        self.userid = userid
        self.password = password
        self.auth = False

    def get_lecture_list(self):
        userId = self.userid
        password = self.password

        login_info = {'userid': userId, 'password': password, 'redirect': '/'}
        base_url = 'https://everytime.kr'

        with requests.Session() as session:
            user_res = session.post(base_url+'/user/login', data=login_info)
            soup = BeautifulSoup(user_res.text, 'html.parser').select('body div')

            # 첫 번째 예외 처리 // 로그인 실패
            if len(soup) == 0:
                return
            
            table_res = session.post(base_url+'/find/timetable/table/list/semester', data={"year":2018, "semester":2})
            
            # 두 번째 예외 처리 // 시간표 없음
            soup = BeautifulSoup(table_res.text, 'lxml')
            id_token = soup.select_one("table")["id"]
            
            if id_token == None:
                return

            lecture_res = session.post(base_url+'/find/timetable/table', data={"id": id_token})
            lecture_soup = BeautifulSoup(lecture_res.text, "html.parser")

            num_list = map(lambda x: x["value"], lecture_soup.select("internal"))
            name_list = map(lambda x: x["value"], lecture_soup.select("name"))
            professor_list = map(lambda x: x["value"], lecture_soup.select("professor"))

            list_var = list(zip(num_list,name_list,professor_list))
            self.auth = True


        return list_var

    def check_auth(self):
        return self.auth

userid = input()
password = input()
list_var = Everytime(userid, password).get_lecture_list()
print(list_var)
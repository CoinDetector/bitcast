import re
import urllib.request
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import sqlite3 as lite


a = ['가상화폐 규제','비트코인','가상화폐']


# database_filename = 'test.db'
# conn = lite.connect(database_filename)
# cs = conn.cursor()

# query = "DROP TABLE IF EXISTS t1"
# cs.execute(query)

# query = 'CREATE TABLE IF NOT EXISTS t1 (id INTEGER PRIMARY_KEY NOT_NULL, Num INTEGER , at DATETIME)'
# cs.execute(query)


def Google():
    count_time = 0
    # 5분 이내인 기사들 갯수 저장하는 데 쓰이는 거라서 Google()함수 실행할 때 처음에만 초기화

    for i in range(len(a)):
        firsttime = True
        # 항상 키워드 첫 검색할 때는 처음 페이지임

        url = 'https://www.google.co.kr/search?q={0}&dcr=0&tbm=nws&source=lnt&tbs=qdr:h&sa=X&ved=0ahUKEwjGzri1gJ7ZAhVCU7wKHXEVDk4QpwUIHQ&biw=645&bih=702&dpr=2'
        # 검색어 바뀔 때마다 검색용 url 초기화

        while bool(url) == True:
            # url이 존재 하면(검색할 url이 있다면)

            if firsttime == True:
                # 첫번째 페이지일 때 초기화 된 url 써야됨
                html = requests.get(url.format(a[i])).text
                soup = BeautifulSoup(html, 'html.parser')
                check = soup.select('#foot a')
                lists = soup.select('#res')
                # check / lists 둘 다 필요함
                # 하나는 다음 페이지가 있는지 검사하고, 다음 페이지 검색할 때 쓰이고
                # 다른 하나는 페이지 내에 기사 시간 가져오기 위해 필요함
                url = ""
                # 필요에 따라 url 지정해 주기 위해 비워줌

                for title in lists:
                    x = title.select('.f')
                    # 이 부분이 시간있는 태그 검사하는 곳
                    for time1 in x:
                        # print(time1.text[-5:])
                        p1 = re.compile('[0-5]+분 전')
                        m1 = p1.search(time1.text[-5:])
                        # p2 = re.compile('[0-9]{0,2}초 전')
                        # m2 = p2.search(time1.text[-5:])
                        # 초 단위도 할 것인가?

                        if (m1 != None) and (len(time1.text[-5:].strip()) == 4):
                            count_time += 1
                            # 구글은 마지막 자리에 시간이 들어가서
                            # 마지막만 4~5자리만 검색해 주면 됨
                            # 정규표현식대로 ~분 전 으로 검색해서 한자리 수라면 맨 앞자리가 null일테니 공백 지우는 strip()써주면 4자리가 될 것이기 때문에 저렇게 써줌
                            # 그래서 해당되면 5분 내 작성된 기사 개수 +1

                firsttime = False
                # 첫번째 페이지 검색 끝났으니까 False로 돌려줌
                # 밑 부분은 할 필요없음


            elif firsttime == False:
                # 두번째 페이지부터는 맨 밑에 '다음'이라는 버튼이 있는 url로 가야됨
                html = requests.get(url).text
                soup = BeautifulSoup(html, 'html.parser')
                check = soup.select('#foot a')
                lists = soup.select('#res')
                url = ""


                for title in lists:
                    x = title.select('.f')
                    for time1 in x:
                        # print(time1.text[-5:])
                        p1 = re.compile('[0-5]+분 전')
                        m1 = p1.search(time1.text[-5:])
                        # p2 = re.compile('[0-9]{0,2}초 전')
                        # m2 = p2.search(time1.text[-5:])
                        # 초 단위도 할 것인가?

                        if (m1 != None) and (len(time1.text[-5:].strip()) == 4):
                            count_time += 1



            ctx = '다음'
            for ini in check:
                if ctx in ini.text:
                    url = "https://www.google.co.kr" + ini.get('href')
                    # 다음페이지 저장하기


        print("*********{0}**********".format(a[i]))
        # 지금까지 어떤 키워드 검색했는지 알려주기





# ========================================== while ============================================
    print("\nFinished")
    print(count_time)

    return count_time



Google()


# query = "INSERT into t1 values (?, ?, DATETIME('NOW','LOCALTIME'))"
# cs.execute(query, (b, Google()))
# conn.commit()

# cs.close()
# conn.close()
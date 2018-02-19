import re
import urllib.request
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime, timedelta
import sqlite3 as lite

keyword = ['비트코인','가상화폐 규제','거래소 폐쇄','급락','하락','폭락','떡락','빗썸','압수수색','규제 강화']

database_filename = 'test.db'
conn = lite.connect(database_filename)
cs = conn.cursor()

query = "DROP TABLE IF EXISTS t1"
cs.execute(query)

query = 'CREATE TABLE IF NOT EXISTS t1 (id INTEGER PRIMARY_KEY NOT_NULL, Google_Num INTEGER , at DATETIME)'
cs.execute(query)

b = 0
id_num = 0
def Google():

    google_count = 0

    for i in range(len(keyword)):

        firsttime = True
        url = 'https://www.google.co.kr/search?q={0}&dcr=0&tbm=nws&source=lnt&tbs=qdr:h&sa=X&ved=0ahUKEwjGzri1gJ7ZAhVCU7wKHXEVDk4QpwUIHQ&biw=645&bih=702&dpr=2'

        while bool(url) == True:
            if firsttime == True:
                html = requests.get(url.format(keyword[i])).text
                soup = BeautifulSoup(html, 'html.parser')
                check = soup.select('#foot a')
                lists = soup.select('#res')
                url = ""

                for title in lists:
                    x = title.select('.f')
                    for time1 in x:
                        p1 = re.compile('[0-5]+분 전')
                        m1 = p1.search(time1.text[-5:])
                        if (m1 != None) and (len(time1.text[-5:].strip()) == 4):
                            google_count += 1
                firsttime = False

            elif firsttime == False:
                html = requests.get(url).text
                soup = BeautifulSoup(html, 'html.parser')
                check = soup.select('#foot a')
                lists = soup.select('#res')
                url = ""

                for title in lists:
                    x = title.select('.f')
                    for time1 in x:

                        p1 = re.compile('[0-5]+분 전')

                        if (m1 != None) and (len(time1.text[-5:].strip()) == 4):
                            google_count += 1

            ctx = '다음'
            for ini in check:
                if ctx in ini.text:
                    url = "https://www.google.co.kr" + ini.get('href')

    return google_count


while True:
    query = "INSERT into t1 values (?, ?, DATETIME('NOW','LOCALTIME'))"
    cs.execute(query, (b, Google()))
    b += 1

    first = cs.execute("SELECT at from t1 limit 1")
    for row1 in first:
        row_first = datetime.strptime(row1[0], '%Y-%m-%d %H:%M:%S')

    last = cs.execute("SELECT at from t1 ORDER BY at DESC limit 1")
    for row2 in last:
        row_last = datetime.strptime(row2[0], '%Y-%m-%d %H:%M:%S')

    diff = row_last-row_first

    if diff > timedelta(minutes=2):
        query = "DELETE from t1 where id=?"
        cs.execute(query, (id_num,))
        id_num += 1

    conn.commit()
    time.sleep(5)

cs.close()
conn.close()
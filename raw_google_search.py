import re
import urllib.request
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import sqlite3 as lite

keyword = ['비트코인','가상화폐 규제','거래소 폐쇄','급락','하락','폭락','떡락','빗썸','압수수색','규제 강화']

def Google():
    count_time = 0


    for i in range(len()):
        firsttime = True
        url = 'https://www.google.co.kr/search?q={0}&dcr=0&tbm=nws&source=lnt&tbs=qdr:h&sa=X&ved=0ahUKEwjGzri1gJ7ZAhVCU7wKHXEVDk4QpwUIHQ&biw=645&bih=702&dpr=2'

        while bool(url) == True:

            if firsttime == True:

                html = requests.get(url.format(a[i])).text
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
                            count_time += 1

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
                        m1 = p1.search(time1.text[-5:])

                        if (m1 != None) and (len(time1.text[-5:].strip()) == 4):
                            count_time += 1



            ctx = '다음'
            for ini in check:
                if ctx in ini.text:
                    url = "https://www.google.co.kr" + ini.get('href')

        print("*********{0}**********".format(a[i]))

    print("\nFinished")
    # print(count_time)

    return count_time

print(Google())
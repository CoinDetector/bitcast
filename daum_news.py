import sys
import urllib.request
from urllib.parse import quote


import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup as Soup

# from konlpy.tag import Twitter
# from collections import Counter

import sqlite3 as lite

import re

a = ['가상화폐','비트코인','규제','거래소 폐쇄','급락','하락','폭락','떡락','빗썸','압수수색','규제 강화']


b = 0

database_filename = 'test2.db'
conn = lite.connect(database_filename)
cs = conn.cursor()


query = 'CREATE TABLE IF NOT EXISTS t1 (id INTEGER PRIMARY_KEY NOT_NULL, name VARCHAR(255), at DATETIME)'
cs.execute(query)


while True:
    count = 0
    j=0
    c=0

    for i in range(len(a)):
        for j in range(len(a)):
            r = requests.get('http://search.daum.net/search?w=news&q={0}&p={1}'.format(a[i],j))


            soup = Soup(r.text, 'html.parser')
            new_coll = soup.find(id='newsColl')
            news_ul = new_coll.find(id="clusterResultUL")


            for li in news_ul.find_all('li'):
                date_tag = li.find(class_='f_nb date')
                dateValue = date_tag.find('span', {"class":"txt_bar"})

                p = re.compile('[0-5]+분') # re 내장모듈 내(.) compile 메서드를 사용.
                m = p.search(dateValue.previous_sibling)

                if m != None:
                   num = dateValue.previous_sibling
                   count += 1

                j += 1




        print("총 기사 갯수 :  {0}".format(count))

        time.sleep(3)

cs.close()
conn.close()
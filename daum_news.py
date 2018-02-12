import sys
import urllib.request
from urllib.parse import quote

import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup as Soup

import sqlite3 as lite

import re

a = ['가상화폐']

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
    before = None
    current = None

    for i in range(len(a)):
        for j in range(len(a)):
            r = requests.get('http://search.daum.net/search?w=news&q={0}&p={1}&cluster=n&DA=STC&s=NS&a=STCF&dc=STC&pg=1&r=1&p=1&rc=1&at=more&sd=20180211153455&ed=20180212153455&period=d'.format(a[i],j))

            soup = Soup(r.text, 'html.parser')
            new_coll = soup.find(id='newsColl')
            news_ul = new_coll.find(id="newsResultUL")

            if before == None:
                before = news_ul.find(class_="wrap_tit mg_tit")
            else:
                if current == None:
                    current = news_ul.find(class_="wrap_tit mg_tit")
                else:
                    before = current
                    current = news_ul.find(class_="wrap_tit mg_tit")
                    if before == current:
                        break
            for li in news_ul.find_all('li'):
                date_tag = li.find(class_='f_nb date')
                dateValue = date_tag.find('span', {"class":"txt_bar"})

                p = re.compile('[0-5]+분') # re 내장모듈 내(.) compile 메서드를 사용.
                m = p.search(dateValue.previous_sibling)

                if m != None:
                   num = dateValue.previous_sibling
                   count += 1

                j += 1

                c += 1

        print("총 기사 갯수 :  {0}".format(count))

        time.sleep(10)

cs.close()
conn.close()
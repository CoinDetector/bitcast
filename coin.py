import sys
import re
import urllib.request
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

import sqlite3 as lite





a = ['가상화폐','비트코인','가상화폐 규제','거래소 폐쇄','급락','하락','폭락','떡락','빗썸','압수수색','규제 강화']

titlelist = []
hreflist = []
b = 0
howmany = 0

database_filename = 'test.db'
conn = lite.connect(database_filename)
cs = conn.cursor()


query = "DROP TABLE IF EXISTS t1"
cs.execute(query)


query = 'CREATE TABLE IF NOT EXISTS t1 (id INTEGER PRIMARY_KEY NOT_NULL, Num INTEGER , at DATETIME)'
cs.execute(query)



while True:



    for i in range(len(a)):
        html = requests.get('https://news.google.com/news/search/section/q/{0}/{1}?hl=ko&gl=KR&ned=kr'.format(a[i], a[i])).text
        soup = BeautifulSoup(html,'html.parser')
        lists = soup.select('div .KaRWed .deQdld c-wiz .lPV2Xe')




        for tag in lists:
            x = tag.select('span .d5kXP')
            # y = tag.select('')
            for ab in x:
                print(ab.text)
                p = re.compile('[0-9]+분 전')
                m = p.search(ab.text)
                if m != None:
                    howmany += 1

            # if tag.text not in titlelist:
            #     titlelist.append(tag.text)


    # for i1 in range(len(titlelist)):

    #     countsum = 0

    #     for i2 in range(len(a)):
    #         countsum += titlelist[i1].count(a[i2])

    query = "INSERT into t1 values (?, ?, DATETIME('NOW','LOCALTIME'))"
    cs.execute(query,(b, howmany))
    conn.commit()
    b += 1
    print(howmany)
    time.sleep(5)



cs.close()
conn.close()
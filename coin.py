# import sys
# from urllib.parse import quote
import re
import urllib.request
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import sqlite3 as lite
import logging
from apscheduler.schedulers.blocking import BlockingScheduler

# a = ['가상화폐','비트코인','가상화폐 규제','거래소 폐쇄','급락','하락','폭락','떡락','빗썸','압수수색','규제 강화']
a = ['google']


#scheduler = BlockingScheduler()

# database_filename = 'test.db'
# conn = lite.connect(database_filename)
# cs = conn.cursor()

# query = "DROP TABLE IF EXISTS t1"
# cs.execute(query)

# query = 'CREATE TABLE IF NOT EXISTS t1 (id INTEGER PRIMARY_KEY NOT_NULL, Num INTEGER , at DATETIME)'
# cs.execute(query)


def Google():
    b = 0
    howmany = 0
    for i in range(len(a)):
        html = requests.get('https://news.google.com/news/search/section/q/{0}/{1}?hl=ko&gl=KR&ned=kr'.format(a[i], a[i])).text
        soup = BeautifulSoup(html, 'html.parser')
        lists = soup.select('div .KaRWed .deQdld c-wiz .lPV2Xe')

        for tag in lists:
            x = tag.select('span .d5kXP')
            for ab in x:
                p = re.compile('[0-5]{0,1}분 전')
                m = p.search(ab.text)
                if (m != None) and (len(ab.text) == 4):
                    howmany += 1





    return howmany
    # b += 1
    # print(Google())


#logging.basicConfig()
#scheduler.add_job(Google,'interval', seconds = 5)
#scheduler.start()

# query = "INSERT into t1 values (?, ?, DATETIME('NOW','LOCALTIME'))"
# cs.execute(query, (b, Google()))
# conn.commit()


# cs.close()
# conn.close()


import sys
import urllib.request
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime



# from konlpy.tag import Twitter
# from collections import Counter

import sqlite3 as lite







# https://news.google.com/news/search/section/q/가상화폐/가상화폐?hl=ko&gl=KR&ned=kr
# https://news.google.com/news/headlines/section/topic/BUSINESS.ko_kr/경제?hl=ko&gl=KR

# while True:
# now = datetime.now()
# print(time.)


a = ['가상화폐','비트코인','규제','거래소 폐쇄','급락','하락','폭락','떡락','빗썸','압수수색','규제 강화']
# 검색할 키워드 & 기준이 될 키워드
now = []
# 시간 넣을 리스트
titlelist = []
# 기사 제목 리스트
hreflist = []
# 기사 주소 리스트



database_filename = 'test.db'
conn = lite.connect(database_filename)
cs = conn.cursor()

# query = 'DROP TABLE IF NOT EXISTS t1'
# cs.execute(query)


query = 'CREATE TABLE IF NOT EXISTS t1 (id INTEGER PRIMARY_KEY NOT_NULL, name VARCHAR(255), at DATETIME)'
cs.execute(query)



while True:
# for i in range(3):
    howmany = 0
    # Warning기사 갯수 초기화


    for i in range(len(a)):
        html = requests.get('https://news.google.com/news/search/section/q/{0}/{1}?hl=ko&gl=KR&ned=kr'.format(a[i], a[i])).text
        # 구글 뉴스 '경제' 파트에서 검색 -- 한글 ver.
        soup = BeautifulSoup(html,'html.parser')
        lists = soup.select('div .KaRWed .deQdld c-wiz .lPV2Xe .v4IxVd a')

        now.append(datetime.now())
        # 키워드 당 검색하는 시간 추가(검색 키워드 : 시간 = 1 : 1)

        for tag in lists:
        # 찾으려는 부분에 있는 기사 제목 & 기사 주소 중에서
            if tag.text not in titlelist:
                titlelist.append(tag.text)
            if tag.get('href') not in hreflist:
                hreflist.append(tag.get('href'))
            # 기존 리스트에 없는 값 추가(제목은 titlelist // 주소는 hreflist)

        # now.append("******************{0}*********************".format(a[i]))
        # titlelist.append("******************{0}*********************".format(a[i]))
        # hreflist.append("******************{0}*********************".format(a[i]))
        # 마지막에 어떤 키워드였는지 리스트 맨 마지막에 추가



        print('========================================{0}========================================'.format(a[i]))
        # 해당 키워드까지 검색 완료

    for i1 in range(len(titlelist)):
        # print(titlelist[i1])
        # titlelist(기사 제목 모음)에 있는 모든 제목 가져오기
        countsum = 0
        # 제목 당 키워드 셀 때 쓰는 숫자 초기화
        for i2 in range(len(a)):
            countsum += titlelist[i1].count(a[i2])
            # 기사제목에 있는 키워드 갯수 세기



        if countsum >= 3:
        # 해당 기사제목에서 키워드중 3개 이상 포함되었을 때 warning 표시
            howmany += 1
            # print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<    Warning    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            # 해당 키워드 3개 이상 포함되었는데 긍정적인 기사일때는 어떻게 할 것인가 생각해보기


    print(now[-1])
    print("총 기사 갯수 :  {0}".format(len(titlelist)))
    print("Warning 기수 갯수 : {0}".format(howmany))

    f = open('test.txt', 'w')
    for write in range(len(titlelist)):

        f.write(titlelist[write])

    f.close()

    time.sleep(3)
    # 5초 후 다시 검색




    chars = titlelist
    for b in range(len(chars)):
        query = "INSERT into t1 values (?, ?, DATETIME('NOW'))"
        cs.execute(query,(b, chars[b]))
    conn.commit()

cs.close()
conn.close()
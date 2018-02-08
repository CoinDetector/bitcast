import requests
from bs4 import BeautifulSoup
import time

titlelist = []

while True:
    a = ['비트코인', '에이다', '스텔라 루멘', '리플', '트론', '가상화폐','정부규제']

    for i in range(len(a)):
        html = requests.get('http://search.daum.net/search?w=news&q={0}&spacing=0'.format(a[i])).text
        soup = BeautifulSoup(html,'html.parser')

        lists = soup.select('.f_link_b')

        for tag in lists:
            if tag.text not in titlelist:
                titlelist.append(tag.text)

    for j in range(len(titlelist)):
        print(titlelist[j])

    print("============================================================")

    print("============================================================")

    print("============================================================")

    print("============================================================")
    print("총 기사 갯수:  {0}".format(len(titlelist)))



    time.sleep(3)


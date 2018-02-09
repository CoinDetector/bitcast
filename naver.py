import requests
import re
from bs4 import BeautifulSoup

keyword = ['가상화폐','가상']

baseURL = 'https://search.naver.com/search.naver?where=news&query='
endURL = '&ie=utf8&sort=1&pd=7'

NextPage = True
NextIndex = 1
for i in range(len(keyword)):
    print("++++++++++++")
    print(keyword[i])
    print("++++++++++++")
    url = baseURL + keyword[i] + endURL
    NextPage = True
    NextIndex = 1
    while NextPage:
        html = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
        if html.status_code == 200:
             soup = BeautifulSoup(html.text, 'html.parser')
             sort = soup.find("ul",{"class": "type01"}).find_all("dd", {"class":"txt_inline"})
             
             
             for article in sort :
                 uploadTime = article.text
                 pattern = re.compile(r'\s+')
                 uploadTime = re.sub(pattern, '', uploadTime)
                 
                 p = re.compile('[0-9]+분전') # re 내장모듈 내(.) compile 메서드를 사용.
                 m = p.search(uploadTime)

                 if m != None:
                     print(m)#테이블에 값 집어넣기
                 else:
                     NextPage = False
                     break
             next = soup.find("div",{"class": "paging"}).find("a", {"class":"next"})
             
             if next == None:
                NextPage = False
             else:
               
                arr = soup.find("div",{"class": "paging"}).find_all("a")[NextIndex].get("href")
                NextIndex += 1
                url = "https:" + arr
                











import requests
import re
from bs4 import BeautifulSoup

keyword = ['가상화폐','비트코인','가상화폐 규제','거래소 폐쇄','급락','하락','폭락','떡락','빗썸','압수수색','규제 강화']

def getNaverInfo():
    baseURL = 'https://search.naver.com/search.naver?where=news&query='
    endURL = '&ie=utf8&sort=1&pd=7'

    NextPage = True
    NextIndex = 1
    naverCount = 0
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
                 isValid = soup.find("div", {"id": "notfound"})
                 
                 if isValid is not None:
                     break
                 else:
                     sort = soup.find("ul",{"class": "type01"}).find_all("dd", {"class":"txt_inline"})
                     
                     
                     for article in sort :
                         sort2 = article.find("span", {"class": "bar"})
    #                     print(sort2.next_sibling)
    #                     uploadTime = article.text
                         timeValue = sort2.next_sibling
    #                     pattern = re.compile(r'\s+')
    #                     uploadTime = re.sub(pattern, '', uploadTime)
    #                     value = re.split(r"[\:\,\.\s]*",uploadTime)

                         p = re.compile('[0-5]+분') # re 내장모듈 내(.) compile 메서드를 사용.
                         m = p.search(timeValue)
                        
                        
                         if m != None and len(sort2.next_sibling) == 6:
                             print(timeValue.previous_sibling)
                             print(timeValue)
                             naverCount += 1
    #                         print(value)#테이블에 값 집어넣기
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
   
    return naverCount

value =  getNaverInfo()
print(value)





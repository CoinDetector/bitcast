import google_search
# import naver
# import daum_news
import logging
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

def search():
    totalCount = 0
    totalCount += google_search.Google()
    print(totalCount)
    # totalCount += naver.getNaverInfo()
    # print(totalCount)
    # totalCount += daum_news.daum_news.daum()
    # print(totalCount)


logging.basicConfig()
scheduler.add_job(search,'interval',seconds=5)
scheduler.start()


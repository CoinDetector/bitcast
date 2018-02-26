import naver
import daum_news
import sqlite3
import pandas as pd
import numpy as np
import plotly
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.offline as offline
import plotly.graph_objs as go
import time


def search():
    totalCount = 0
    totalCount += naver.getNaverInfo()
    totalCount += daum_news.daum()
    print(totalCount)
    return totalCount



database_filename = 'LetsMakeChart.db'
conn = sqlite3.connect(database_filename)
cursor = conn.cursor()

query = "DROP TABLE IF EXISTS t1"
cursor.execute(query)

query = 'CREATE TABLE IF NOT EXISTS t1 (id INTEGER PRIMARY_KEY NOT_NULL, Google_Num INTEGER , at DATETIME)'
cursor.execute(query)



b = 0
id_num = 0
while True:

    query = "INSERT into t1 values (?, ?, DATETIME('NOW','LOCALTIME'))"
    cursor.execute(query, (b, search()))
    b += 1

    conn.commit()
    print("finish")


    cursor.execute("SELECT Google_Num, at FROM t1")
    rows = cursor.fetchall()

    df = pd.DataFrame([[ij for ij in i] for i in rows])
    df.rename(columns={0: 'Google_Num', 1: 'at'}, inplace=True)

    trace1 = go.Scatter(
        x=df['at'],
        y=df['Google_Num'],
        connectgaps=True,
        mode="lines+markers",
        marker=dict(
            color=np.random.randn(500),
            colorscale='Viridis',
            symbol="144",
        ),
    )
    layout = go.Layout(
        xaxis=XAxis(title='시간' ),
        yaxis=YAxis(type='linear', title='갯수' ),
        title="시간당 기사 갯수 세기",
    )
    data = [trace1]
    fig = go.Figure(data=data, layout=layout)

    offline.plot(fig, filename='Count_Chart.html', auto_open=False, show_link=False)

    time.sleep(5)


cs.close()
conn.close()
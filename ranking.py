import requests
from bs4 import BeautifulSoup

import pandas as pd


url = 'https://scraping-for-beginner.herokuapp.com/ranking/'

# レスポンス取得
res = requests.get(url)

# BeautifulSoupでレスポンスをHTMLの構造に変換する
soup = BeautifulSoup(res.text, 'html.parser')

# 1つの観光地情報の取得
spots = soup.select('.u_areaListRankingBox')
spot = spots[0]

# 観光地名
spot_name = spot.find('div', attrs={'class': 'u_title'})
# 観光地のタイトルからspanを抽出する
spot_name.find('span', attrs={'class': 'badge'}).extract()
spot_name = spot_name.text.replace('\n', '')
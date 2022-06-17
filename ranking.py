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

# 評点
eval_num = float(spot.find('div', attrs={'class': 'u_rankBox'}).text.replace('\n', ''))

# 観光地情報を格納する辞書
datum = {}

# 各カテゴリー評価
category_items = spot.find('div', attrs={'class': 'u_categoryTipsItem'})
category_items = category_items.find_all('dl')

for category_item in category_items:

  print(category_item)
  # 各カテゴリーの要素を取得
  category = category_item.dt.text
  rank = float(category_item.span.text)
  
  # カテゴリー情報を辞書に格納
  datum[category] = rank

# 観光地情報を辞書に格納
datum['観光地名'] = spot_name
datum['評点'] = eval_num
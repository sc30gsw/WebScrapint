import requests
from bs4 import BeautifulSoup

import pandas as pd


url = 'https://scraping-for-beginner.herokuapp.com/ranking/'

# レスポンス取得
res = requests.get(url)

# BeautifulSoupでレスポンスをHTMLの構造に変換する
soup = BeautifulSoup(res.text, 'html.parser')

# 観光地情報の取得
spots = soup.select('.u_areaListRankingBox')

# 観光地の全情報を格納するリスト
data = []

for spot in spots:
  # 観光地名
  spot_name = spot.find('div', attrs={'class': 'u_title'})
  # 観光地のタイトルからspanを抽出する
  spot_name.find('span', attrs={'class': 'badge'}).extract()
  spot_name = spot_name.text.replace('\n', '')

  # 評点
  eval_num = float(spot.find('div', attrs={'class': 'u_rankBox'}).text.replace('\n', ''))
  
  # 各カテゴリー評価
  category_items = spot.find('div', attrs={'class': 'u_categoryTipsItem'})
  category_items = category_items.find_all('dl')

  # 観光地情報を格納する辞書
  datum = {}

  for category_item in category_items:
    # 各カテゴリーの要素を取得
    category = category_item.dt.text
    rank = float(category_item.span.text)
    
    # カテゴリー情報を辞書に格納
    datum[category] = rank
  
  # 観光地情報を辞書に格納
  datum['観光地名'] = spot_name
  datum['評点'] = eval_num
  
  # 観光地情報の辞書をリストに追加する
  data.append(datum)

# 観光地情報のリストをDataFrameに渡す
df = pd.DataFrame(data)

# 列を入れ替え、表示する順を変更する
# 元の列 : df[['楽しさ', '人混みの多さ', '景色', 'アクセス', '観光地名', '評点']]
df = df[['観光地名', '評点', '楽しさ', '人混みの多さ', '景色', 'アクセス']]

df.to_csv('./data/観光地情報.csv', index=False)
import requests
from bs4 import BeautifulSoup

import pandas as pd


url = 'https://scraping-for-beginner.herokuapp.com/ranking/'

# レスポンス取得
res = requests.get(url)

# BeautifulSoupでレスポンスをHTMLの構造に変換する
soup = BeautifulSoup(res.text, 'html.parser')
import requests
from bs4 import BeautifulSoup

url = 'https://scraping-for-beginner.herokuapp.com/udemy'

# レスポンス取得
res = requests.get(url)
# レスポンスのHTMLを取得
# print(res.text)

# BeautifulSoupでレスポンスをHTMLの構造に変換する
soup = BeautifulSoup(res.text, 'html.parser')
soup.find_all('p', attrs={'class': 'subscribers'})

# ページ上の受講生数を取得
subscribers = soup.select('.subscribers')[0]
n_subscribers = int(subscribers.text.split('：')[1])

# ページ上のレビュー数を取得
reviews = soup.select('.reviews')[0]
n_reviews = int(reviews.text.split('：')[1])
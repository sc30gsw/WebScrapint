from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

import config

# ブラウザの起動
browser = webdriver.Chrome()

# 指定したWebページアクセスする
url = 'https://scraping-for-beginner.herokuapp.com/login_page'
browser.get(url)
sleep(3)

# アクセスしたWebページの要素を取得
elem_username = browser.find_element(By.ID, 'username')
elem_password = browser.find_element(By.ID, 'password')
elem_login_btn = browser.find_element(By.ID, 'login-btn')

# 取得した要素に対してキーを送信
# usernameとpasswordを入力
elem_username.send_keys(config.INTRO_USERNAME)
elem_password.send_keys(config.INTRO_PASSWORD)
sleep(1)

# ログインボタンをクリックする
elem_login_btn.click()
sleep(1)

# Webページの情報を取得する
# tdタグを取得
elems_td = browser.find_elements(By.TAG_NAME, 'td')
# thタグを取得
elems_th = browser.find_elements(By.TAG_NAME, 'th')

# 取得要素のテキスト情報を各リストに格納する
keys = [elem_th.text for elem_th in elems_th]
values = [elem_td.text for elem_td in elems_td]

df = pd.DataFrame()
# 列に各リストを設定
df['項目'] = keys
df['値'] = values

# csvに出力する
df.to_csv('./data/講師情報.csv')


# ブラウザを閉じる
browser.quit()
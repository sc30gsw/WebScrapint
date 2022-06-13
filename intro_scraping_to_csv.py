from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

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
sleep(4)

# ブラウザを閉じる
browser.quit()
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
sleep(1)

# Webページの情報を取得する
elem_name = browser.find_element(By.ID, 'name')
elem_company = browser.find_element(By.ID, 'company')
elem_birthday = browser.find_element(By.ID, 'birthday')
elem_come_from = browser.find_element(By.ID, 'come_from')
elem_hobby = browser.find_element(By.ID, 'hobby')

# 取得要素のテキスト情報を取得
name = elem_name.text
company = elem_company.text
birthday = elem_birthday.text
come_from = elem_come_from.text
hobby = elem_hobby.text

# ブラウザを閉じる
browser.quit()
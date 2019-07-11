from selenium import webdriver
import os

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("http://0.0.0.0:5000/my-chatroom")
while True:
    user_input = input('refresh > ')
    driver.refresh()

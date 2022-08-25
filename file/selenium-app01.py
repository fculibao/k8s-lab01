from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(executable_path="./home/ferdie/selenium-project/chromedriver")
browser.get("http://192.168.1.229:8080/vproapp/login")
print('Title: %s' % browser.title)

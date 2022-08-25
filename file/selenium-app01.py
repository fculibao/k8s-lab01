
from selenium import webdriver

PATH = "/home/ferdie/selenium-project/chromedriver*"
driver = webdriver.Chrome(PATH)

driver.get("http://192.168.1.229:8080/vproapp/login") 
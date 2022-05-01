from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()

path = "/home/elakia/softwares/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(path)

driver.get("https://www.linkedin.com/login")

email = os.environ.get('email')

password =os.environ.get('password')

username = driver.find_element_by_id("username")

pw = driver.find_element_by_id("password")

username.send_keys(email)

pw.send_keys(password)

# driver.find_element_by_class_name("btn__primary--large from__button--floating").click()
pw.send_keys(Keys.RETURN)
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

path = "/home/elakia/softwares/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(path)

driver.get("https://google.com")


que = driver.find_element_by_name("q")

que.send_keys("chicken biryani")

time.sleep(3)

que.send_keys(Keys.ARROW_DOWN)

que.send_keys(Keys.RETURN)

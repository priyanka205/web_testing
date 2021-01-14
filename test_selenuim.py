from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# driver = webdriver.Firefox()
driver = webdriver.Chrome()#from which browser
driver.get("http://www.python.org")#get the link and open that website
assert "Python" in driver.title#
elem = driver.find_element_by_name("q")#we can write here path it can be by class,xpath etc
elem.clear()#if there is already written something then this will clean it
elem.send_keys("pycon")#send what we want to see
elem.send_keys(Keys.RETURN)#its like entering
sleep(10)
assert "No results found." not in driver.page_source
driver.close()
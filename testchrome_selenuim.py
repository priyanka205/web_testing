#for path we mostly use xpath because its give you the exact location/unique
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# driver = webdriver.Firefox()
driver = webdriver.Chrome()#from which browser
driver.get("https://www.google.com/")#get the link and open that website
driver.maximize_window()

#elem = driver.find_element_by_name("q")#inspect and see what the name is there(by usine name)
elem = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")#we nedd to give single quote for tsf(by using x path)
elem.clear()#if there is already written something then this will clean it
elem.send_keys("python selenuim tutorials")#send what we want to see
elem.send_keys(Keys.RETURN)#its like entering
sleep(10)
driver.close()
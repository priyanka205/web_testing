from selenium import webdriver
from time import sleep
# from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get('https://www.w3schools.com/')
sleep(3)

login = driver.find_element_by_xpath('//*[@id="loginactioncontainer"]').click()
driver.maximize_window()
sleep(2)

username = driver.find_element_by_xpath('//*[@id="loginform"]/div[2]/input')
username.send_keys('priyanka.shrestha321@gmail.com')
sleep(2)

password = driver.find_element_by_xpath('//*[@id="loginform"]/div[4]/input')
password.send_keys('Nepal510')
sleep(2)

demo = driver.find_element_by_xpath('//*[@id="login_submit_button"]').click()
sleep(3)


pythontitle = driver.find_element_by_xpath('//*[@id="mySidenav"]/div/a[24]').click()
sleep(2)



courses = driver.find_elements_by_xpath('//*[@id="leftmenuinnerinner"]/a')
for course in courses:
    print(course.text)














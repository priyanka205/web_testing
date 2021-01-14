from selenium import webdriver
from time import sleep



driver = webdriver.Chrome()
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp")
sleep(2)

firstname = driver.find_element_by_xpath('//*[@id="firstName"]')
firstname.send_keys("priyanka")
sleep(2)

lastname = driver.find_element_by_xpath('//*[@id="lastName"]')
lastname.send_keys("shrestha")
sleep(2)

email = driver.find_element_by_xpath('//*[@id="username"]')
email.send_keys("priyanka154378")
sleep(2)

password = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input')
password.send_keys("nEpal506")
sleep(2)

confirm = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
confirm.send_keys("nEpal506")
sleep(2)

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[3]/div/div[1]/div/div/div[1]/div/div/input').click()
sleep(2)

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]').click()
sleep(2)

driver.close()


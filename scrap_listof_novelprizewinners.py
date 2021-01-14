from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

driver.get('https://en.wikipedia.org/wiki/List_of_Nobel_Peace_Prize_laureates')
sleep(2)

for i in range(51):
    try:
         name = driver.find_element_by_xpath(f'//tr[{i+1}]/td/b/a').text
         print(name)
    except:
        continue







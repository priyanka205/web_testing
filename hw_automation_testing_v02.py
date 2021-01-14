# Automate this using selenium python. Randomly choose the answer.
from selenium import webdriver
from time import sleep
import random
import sys
# from selenium.webdriver import 
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://www.16personalities.com/free-personality-test')

# sleep(2)
driver.maximize_window()

progress_percentage = ""

def select_option():
    select_questions = driver.find_elements_by_xpath('//*[@class="options"]')
    for questions in select_questions:
        options = questions.find_elements_by_xpath('.//div[@role="radio"]')
        random_select = random.choice(options)
        random_select.click()
        sleep(1)
        progress_percentage = driver.find_element_by_xpath('//*[@id="progress-wrapper"]').text

    try:
        next_button = driver.find_element_by_xpath('//button[@type="button"]')
        next_button.click()
        sleep(2)
    except:
        pass



while progress_percentage != "100%":
    select_option()

# select_questions = driver.find_elements_by_xpath('//*[@class="options"]')
# for questions in select_questions:
#     options = questions.find_elements_by_xpath('.//div[@role="radio"]')
#     random_select = random.choice(options)
#     random_select.click()
#     sleep(1)

driver.find_element_by_xpath("//div[@id='sl_opt_1_u2eehiawns']").click()

# see_result = driver.find_element_by_xpath('//*[@id="main-app"]/main/div[1]/div/div[4]/button').click()
driver.find_element_by_xpath('//button[@class="btn start btn-action"]').click()
# sleep(2)



#Click start reading button
driver.find_element_by_xpath('//*[@class="fal fa-arrow-down"]').click()
sleep(1)

#Click sure button
driver.find_element_by_xpath("//button[@dusk='yes']").click()
sleep(1)

#Provide email address
email_input = driver.find_element_by_xpath("//input[@placeholder='your@email.com']")
email_input.clear()
email_input.send_keys("your@email.com")
sleep(1)

#Click submit button
driver.find_element_by_xpath("//button[@class='btn btn-action'][@type='button']").click()
sleep(1)


# #No Thanks
# driver.find_element_by_xpath('//button[@dusk="no"]')
# driver.close()
# sys.exit()





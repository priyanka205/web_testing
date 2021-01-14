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
# driver.maximize_window()

progress_percentage = ""

# with open("question_with_answer.csv", "w") as wf:
#     header = ["Question", "Answer"]
#     header_line = ",".join(header)
#     wf.write(header_line)
#     wf.write("\n")
    

def select_option():
    global progress_percentage

    question_object = driver.find_elements_by_xpath('//*[@class="statement"]')
    # questions  = question_object.replace(",", "")

    # print("question")
    # print(question_object[0].text)
    question_list = []
    for question in question_object:
        question_list.append((question.text).replace(",",""))


    select_answers = driver.find_elements_by_xpath('//*[@class="options"]')
    answer_list = []
    # for answer in select_answers:
    #     answer_list.append(answer.get_attribute("aria-label"))


    # print("selection")
    # print(select_answers[0].text)
  
    for options in select_answers:
        radio_buttons = options.find_elements_by_xpath('.//div[@role="radio"]')
        # print("options")
        # print(options.text)
        # sys.exit()
        random_select = random.choice(radio_buttons)
        answer_clicked = random_select.get_attribute("aria-label")
        answer_list.append(answer_clicked)
        random_select.click()
        sleep(1)
        progress_percentage = driver.find_element_by_xpath('//*[@id="progress-wrapper"]').text

    try:
        next_button = driver.find_element_by_xpath('//button[@type="button"]')
        next_button.click()
        sleep(2)
    except:
        pass

    return question_list, answer_list



with open("question_with_answer.csv", "w") as wf:
    header = ["Question", "Answer"]
    header_line = ",".join(header)
    wf.write(header_line)
    wf.write("\n")

    while progress_percentage != "100%":
        print(progress_percentage)
        question_list, answer_list = select_option()


        for n,ques in enumerate(question_list):
            data_to_write=[ques, answer_list[n]]
            wf.write(','.join(data_to_write))
            wf.write("\n")


# driver.find_element_by_xpath("//div[@id='sl_opt_1_u2eehiawns']").click()

# see_result = driver.find_element_by_xpath('//*[@id="main-app"]/main/div[1]/div/div[4]/button').click()
# driver.find_element_by_xpath('//button[@dusk="submit-button"]').click()
# sleep(2)

#Click start reading button
driver.find_element_by_xpath('//button[@dusk="close-results"]').click()
sleep(1)

# #No Thanks
driver.find_element_by_xpath('//button[@dusk="no"]').click()



with open("explore_this_type.text", "w") as wf:
    article = driver.find_element_by_xpath("//article[@class='main description']").text
    print(article)
    wf.write("main description\n")
    wf.write(article)
    wf.write("\n\n")


    topic_list = ["strength","romantic","friendship","parenthood","carrer","workplace","conclusion"]
  
    for topic in topic_list:
        driver.find_element_by_xpath('//div[@class="fal fa-long-arrow-right"]').click()
        # strength = driver.find_element_by_xpath("//article[@class='main description']").text
        topic_description = driver.find_element_by_xpath("//article[@class='main description']").text
        # topic_list = ("\n")
        #next

        # print(strengeth)
        # wf.write("main strength\n")
        # wf.write(topic)
        wf.write(topic_description)
        wf.write("\n\n")

    
    driver.find_element_by_xpath('//div[@class="fal fa-long-arrow-right"]').click()
    premium =  driver.find_element_by_xpath('//*[@class="intro"]').text
    # print(premium)
    # wf.write("premium profile\n")
    wf.write(premium)
    wf.write("\n\n")



#Click sure button
driver.find_element_by_xpath("//button[@dusk='yes']").click()
sleep(1)

#Provide email address
email_input = driver.find_element_by_xpath("//input[@placeholder='your@email.com']")
email_input.clear()
email_input.send_keys("priyanka.shrestha321@gmail.com.com")
sleep(1)

#Click submit button
driver.find_element_by_xpath("//button[@class='btn btn-action'][@type='button']").click()
sleep(1)



# driver.close()
# sys.exit()





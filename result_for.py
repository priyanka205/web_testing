from selenium import webdriver
from time import sleep
import random
import sys
from urllib import request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome()
delay = 10

driver.get("https://www.16personalities.com/isfp-personality")
sleep(2)
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
        #next

        # print(strengeth)
        # wf.write("main strength\n")
        wf.write(topic)
        wf.write(topic_description)
        wf.write("\n\n")

    
    driver.find_element_by_xpath('//div[@class="fal fa-long-arrow-right"]').click()
    premium =  driver.find_element_by_xpath('//*[@class="intro"]').text
    # print(premium)
    # wf.write("premium profile\n")
    wf.write(premium)
    wf.write("\n\n")


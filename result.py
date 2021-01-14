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

    #next
    driver.find_element_by_xpath('//div[@class="fal fa-long-arrow-right"]').click()

    strength = driver.find_element_by_xpath("//article[@class='main description']").text
    # print(strengeth)
    # wf.write("main strength\n")
    wf.write(strength)
    wf.write("\n\n")


    driver.find_element_by_xpath('//div[@class="fal fa-long-arrow-right"]').click()

    romantic =  driver.find_element_by_xpath("//article[@class='main description']").text
    # print(romantic)
    # wf.write("romantic\n")
    wf.write(romantic)
    wf.write("\n\n")

    driver.find_element_by_xpath('//div[@class="fal fa-long-arrow-right"]').click()

    friendship =  driver.find_element_by_xpath("//article[@class='main description']").text
    # print(friendship)
    # wf.write("friendship\n")
    wf.write(friendship)
    wf.write("\n\n")

    driver.find_element_by_xpath('//div[@class="fal fa-long-arrow-right"]').click()



    parenthood =  driver.find_element_by_xpath("//article[@class='main description']").text
    # print(parenthood)
    # wf.write("parenthood\n")
    wf.write(parenthood)
    wf.write("\n\n")
    

    driver.find_element_by_xpath('//div[@class="fal fa-long-arrow-right"]').click()


    career =  driver.find_element_by_xpath("//article[@class='main description']").text
    # print(career)
    # wf.write("career\n")
    wf.write(career)
    wf.write("\n\n")

    driver.find_element_by_xpath('//div[@class="fal fa-long-arrow-right"]').click()


    workpalce =  driver.find_element_by_xpath("//article[@class='main description']").text
    # print(workpalce)
    # wf.write("workpalce\n")
    wf.write(workpalce)
    wf.write("\n\n")

    driver.find_element_by_xpath('//div[@class="fal fa-long-arrow-right"]').click()


    conclusion =  driver.find_element_by_xpath("//article[@class='main description']").text
    # print(conclusion)
    # wf.write("main conclusion\n")
    wf.write(conclusion)
    wf.write("\n\n")

    driver.find_element_by_xpath('//div[@class="fal fa-long-arrow-right"]').click()

    premium =  driver.find_element_by_xpath('//*[@class="intro"]').text
    # print(premium)
    # wf.write("premium profile\n")
    wf.write(premium)
    wf.write("\n\n")












from selenium import webdriver
from time import sleep
import random
import sys
from urllib import request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating")

# number_of_movies = driver.find_elements_by_xpath('//*[@class="lister-item-header"]')


# we are using here try and except beacuse incase xpath is not same with others and to avoid error
def get_movie_details(n):
    movie = driver.find_element_by_xpath(f"//*[@id='main']/div/div[3]/div/div[{n+1}]/div[3]/h3/a")
    movie.click()
    try:
        movie_name = driver.find_element_by_xpath("//div[@class='title_wrapper']/h1").text
    except: 
        movie_name = "Could not load."

    try:
        movie_release_date = driver.find_element_by_xpath('//*[@id="titleYear"]/a').text
    except:
        movie_release_date = "could not load"

    try:
        movie_rating = driver.find_element_by_xpath('//*[@class="ratingValue"]/strong/span').text
    except:
        movie_rating = "could not load"

    try:
        movie_hour = driver.find_element_by_xpath('//*[@id="title-overview-widget"]//time').text
    except:
        movie_hour = "could not load"

    try:
        movie_hour = driver.find_element_by_xpath('//*[@id="title-overview-widget"]//time').text
    except:
        movie_hour = "could not load"


    try:
        movie_genre = driver.find_element_by_xpath('//div[@class="subtext"]/a').text
    except:
        movie_genre = "could not find"

    movie_details = [movie_name, movie_release_date, movie_rating, movie_hour, movie_genre]
    movie_details_line = ",".join(movie_details)

    
       # get the image source
    movie_img = driver.find_element_by_xpath('//*[@class="poster"]/a/img')
    src = movie_img.get_attribute('src')

    # download the image
    image_name = movie_name.replace(":", "")
    request.urlretrieve(src,f".//movie_image//{image_name}.png")


    return movie_details_line
 
def sleep_time():
    time_to_sleep = random.randint(2,10)
    print(f"Sleeping for {time_to_sleep} seconds.")
    sleep(time_to_sleep)

with open("top50movies1.csv", "w") as wf:
    header = ["Movie Name", "Release Date", "Ratings", "Movie Time", "Genre"]
    header_line = ",".join(header)
    wf.write(header_line)
    wf.write("\n")
    try:
        next_button = driver.find_element_by_xpath("//div[@class='desc']/a[@class='lister-page-next next-page']")    
    except:
        next_button = ""
    while next_button != "":
        number_of_movies = driver.find_elements_by_xpath('//*[@class="lister-item-header"]')
# if wants to check next button is working or not: for i in range(len(number_of_movies)-48):
        for i in range(len(number_of_movies)+1):
        # for i in range(1):
            final_line = get_movie_details(i)
            wf.write(final_line)
            wf.write("\n")
            driver.back()
            sleep_time()
        try:
            next_button = driver.find_element_by_xpath("//div[@class='desc']/a[@class='lister-page-next next-page']")
            next_button.click()
        except:
            next_button = ""
        sleep_time()
sleep_time()
driver.close()


## Timer Options
#1) Randomize time value
# time_to_sleep = random.randint(2,10)
# print(f"Sleeping for {time_to_sleep} seconds.")
# sleep(time_to_sleep)
#or  sleep(random.randint(2,10)) directly

# 2) Wait 
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.XPATH, "//div[@class='title_wrapper']/h1"))
#     )
# except:
#     Do something.
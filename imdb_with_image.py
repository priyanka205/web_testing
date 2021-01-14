from selenium import webdriver
from time import sleep
import random
import sys
from urllib import request

driver = webdriver.Chrome()

driver.get("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating")

number_of_movies = driver.find_elements_by_xpath("//*[@id='main']/div/div[3]/div/div/div/h3/a")

def get_movie_details(n):
    movie = driver.find_element_by_xpath(f"//*[@id='main']/div/div[3]/div/div[{n+1}]/div[3]/h3/a")
    movie.click()

    movie_name = driver.find_element_by_xpath("//div[@class='title_wrapper']/h1").text

    movie_release_date = driver.find_element_by_xpath('//*[@id="titleYear"]/a').text
    
    movie_rating = driver.find_element_by_xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[1]/div[1]/div[1]/strong/span').text

    movie_director = driver.find_element_by_xpath('//*[@id="title-overview-widget"]/div[2]/div[1]/div[2]/a').text

    movie_hour = driver.find_element_by_xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[2]/div[2]/div/time').text

    movie_genre = driver.find_element_by_xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[2]/div[2]/div/a[1]').text


    
    movie_details = [movie_name, movie_release_date, movie_rating, movie_director, movie_hour, movie_genre]
    movie_details_line = ",".join(movie_details)

    # get the image source
    movie_img = driver.find_element_by_xpath('//*[@class="poster"]/a/img')
    src = movie_img.get_attribute('src')

    # download the image
    image_name = movie_name.replace(":", "")
    request.urlretrieve(src,f".//movie_image//{image_name}.png")

   

    return movie_details_line


with open("top50movies_02.csv", "w") as wf:
    header = ["Movie Name", "Release Date", "Ratings", "Director By", "Movie Hour", "Genre"]
    header_line = ",".join(header)
    wf.write(header_line)
    wf.write("\n")
    try:
        next_button = driver.find_element_by_xpath("//div[@class='desc']/a[@class='lister-page-next next-page']")    
    except:
        next_button = ""
    while next_button != "":
        for i in range(len(number_of_movies)+1):
        # for i in range(1):
            final_line = get_movie_details(i)
            wf.write(final_line)
            wf.write("\n")
            sleep(random.randint(2,10))
        try:
            next_button = driver.find_element_by_xpath("//div[@class='desc']/a[@class='lister-page-next next-page']")
            next_button.click()
        except:
            next_button = ""
        sleep(random.randint(2,10))

sleep(random.randint(2,10))




# driver.close()
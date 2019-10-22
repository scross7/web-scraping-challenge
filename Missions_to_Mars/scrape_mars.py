from bs4 import BeautifulSoup
import requests
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time

def init_browser():
    executable_path = {'executable_path': './chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape_info():
    executable_path = {'executable_path': './chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    ### NASA Mars News ###
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all('div', class_='content_title')
    title = titles[0].a.text

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    paras = soup.find_all('div', class_='article_teaser_body')
    para = paras[0].text

    ### JPL Mars Space Images - Featured Image ###
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # click button to next page
    browser.find_by_id("full_image").click()

    #give page time to load before searching
    time.sleep(5)

    # search for the next button to click
    browser.find_link_by_partial_text("more info").click()

    #search the new page
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # find the image link
    image = soup.find_all(class_='lede')
    image = "https://www.jpl.nasa.gov" + image[0].a["href"]

    ### Mars Weather ###
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # search the page
    weather = soup.find_all('p', class_='TweetTextSize')

    # find the weather information
    weather = weather[0].text

    # format the weather information
    weather = weather.replace("\n", " ")
    head, sep, tail = weather.partition(' hPapic')
    weather = head

    ### Mars Facts ###
    url = "https://space-facts.com/mars/"

    # read the table with oandas to html
    facts = pd.read_html(url)
    facts = facts[0]
    facts = facts.to_html(index=False)

    ### Mars Hemispheres ###
    # Cerberus Hemisphere Enhanced
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # find the hemisphere thumbnail image and click to next page
    browser.find_by_css('img[class="thumb"]')[0].click()

    # navigate to the next page and search
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # find the hemisphere title on the page
    cerberus_title = soup.find_all('h2', class_='title')[0].text

    # find the link to the image on the page
    cerberus_img = soup.find_all('img', class_="wide-image")
    cerberus_img = "https://astrogeology.usgs.gov" + cerberus_img[0]["src"]

    # Schiaparelli Hemisphere Enhanced
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # find the hemisphere thumbnail image and click to next page
    browser.find_by_css('img[class="thumb"]')[1].click()

    # navigate to the next page and search
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # find the hemisphere title on the page
    Schiaparelli_title = soup.find_all('h2', class_='title')[0].text

    # find the link to the image on the page
    Schiaparelli_img = soup.find_all('img', class_="wide-image")
    Schiaparelli_img = "https://astrogeology.usgs.gov" + Schiaparelli_img[0]["src"]

    # Syrtis Major Hemisphere Enhanced
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # find the hemisphere thumbnail image and click to next page
    browser.find_by_css('img[class="thumb"]')[2].click()

    # navigate to the next page and search
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # find the hemisphere title on the page
    Syrtis_title = soup.find_all('h2', class_='title')[0].text

    # find the link to the image on the page
    Syrtis_img = soup.find_all('img', class_="wide-image")
    Syrtis_img = "https://astrogeology.usgs.gov" + Syrtis_img[0]["src"]

    # Valles Marineris Hemisphere Enhanced
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # find the hemisphere thumbnail image and click to next page
    browser.find_by_css('img[class="thumb"]')[3].click()

    # navigate to the next page and search
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # find the hemisphere title on the page
    Valles_title = soup.find_all('h2', class_='title')[0].text

    # find the link to the image on the page
    Valles_img = soup.find_all('img', class_="wide-image")
    Valles_img = "https://astrogeology.usgs.gov" + Valles_img[0]["src"]

    
    img_dict = [
        {"title": cerberus_title , "img_url": cerberus_img },
        {"title": Schiaparelli_title , "img_url": Schiaparelli_img },
        {"title": Syrtis_title , "img_url": Syrtis_img },
        {"title": Valles_title , "img_url": Valles_img }
    ]


    # Store data in a dictionary
    mars_info_dict = { "title" : title,
                    "para" : para,
                    "image" : image,
                    "weather" : weather,
                    "facts" : facts,
                    "img_dict" : img_dict
                    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_info_dict

if __name__ == "__main__":
    print(scrape_info())
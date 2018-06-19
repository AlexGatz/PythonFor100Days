# This program is intended to be a reusable/modifiable data scraper to collect data for machine learning based projects. 

# Version: 1.1
# Date: 6/10/2018
# Created by: Alex J. Gatz

#TODO: finish base code with the goal of extracting a name and some other data from twitter perhaps?
#TODO: create structured user input
#TODO: find cleaner way to step thought url's that is cleaner than encapsulating everything in a for loop

import sys

# beautifulsoup
from bs4 import BeautifulSoup as bs

# lxml for parsing
import lxml 

# requests to more easily handle url based tasks
import requests as req

# csv library to easily work with csv files
import csv

def main():

    # URL to scrape
    url = 'http://guimp.com/pong_flash.html' 

    # Query the url to return the HTML
    page = req.get(url)

    # Store the HTML in beautifulsoup's format using requests .content for binary data instead of .text for unicode
    soup = bs(page.content, "lxml")

    # 'find_all()' searches in the soup tree for all instances of the search parameter
    # output is a list of html lines
    testSoup = soup.find_all('param')


    #TEST: attempt output to terminal using "prettify"
    #print(soup.prettify()) #TEST_RESULT: success using 'http://guimp.com/' as the url

    #TEST: print output of soup.find_all() to see how it looks
    #print(testSoup) #TEST_RESULT: output resembles lines of html ex. <param .... />

    # Used a bash command for fun to try to grep some information
    # python Scraper.py >> randomsite.txt
    # cat randomsite.txt | grep "put text here" 
    # UPDATE: bash command replaced by find_all()

    # Opens/creates new file
    # "with" ensures that the file is properly closed once the block of code within it is completed
    with open('test.csv', 'w', newline='') as f:

        # Uses the default ',' to separate columns... adds args to csv.writer for more functionality
        testWriter = csv.writer(f)

        # Stepts through each part in the testSoup list and places name and value amounts into a csv
        for names in testSoup:
            testWriter.writerow([names.get('name')] + [names.get('value')])

if __name__ == "__main__":
    main()

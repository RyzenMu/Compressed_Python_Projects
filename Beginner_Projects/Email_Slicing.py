import time
import requests
from bs4 import BeautifulSoup

html_page = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

# print(html_page)

soup = BeautifulSoup(html_page, 'lxml')

print(soup)
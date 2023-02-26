import requests
from bs4 import BeautifulSoup

w3_web_page = requests.get('https://www.w3schools.com/python/module_requests.asp').text

soup = BeautifulSoup(w3_web_page, 'lxml')

courses = soup.findAll('a', target = '_blank')

for course in courses:

    print(course)
    print(course)

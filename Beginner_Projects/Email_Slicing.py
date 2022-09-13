# import requests
import requests

#import Beautiful Soup using pip install beautifulsoup4
from bs4 import BeautifulSoup

#import re
import re

#import lxml
import lxml




# get request from a webpage
page = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=')

#print responce code to the request
print(page)


#Getting contents of a page
page_content = page.content

# print(page_content)


# arrange the page in readable format using Beautifulsoup

bs = BeautifulSoup(page_content, 'lxml')

print(bs.prettify())









# arrange email in an array/dictionary/set

# validate the emails using regex
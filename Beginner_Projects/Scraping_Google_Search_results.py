import requests
from bs4 import BeautifulSoup

google_page = requests.get('https://www.google.com/search?channel=fs&client=ubuntu&q=how+to+find+email+in+facebook+profile').text

soup = BeautifulSoup(google_page, 'lxml')

results = soup.findAll('a')

for result in results:
    print(result.text)
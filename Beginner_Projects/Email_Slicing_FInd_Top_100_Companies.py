#  1. Find a webpage which has a list of top 100 companies
#  2. Send Request to the webpage
#  3. collect the html data from the web page
#  4. use Beautiful soul and prettier() to find only the companies list 
#  5. store the companies in a list
#  6. use request and enter into 100 webpages
#  7. get webpage of 100 companies
#  8. collect the html data of 100 companies
#  9. find the email using regular expressions re module.
#  10.The End


#1.
from ctypes import sizeof
from urllib import response
import requests
from bs4 import BeautifulSoup
import re


forbes_website = requests.get('https://www.forbes.com/lists/global2000/?sh=3951212a5ac0').text



#2.
# prints the response code of the forbes website
# print(forbes_website)



#3.
soup = BeautifulSoup(forbes_website, 'html.parser')

all_divs = soup.find_all('div', class_="organizationName second table-cell name")


# for s_no, divs in enumerate(all_divs):
#     print(s_no, divs.text)


#4.
# prettier is not installed



#5.
company_list = []

for divs in all_divs:
    company_list.append(divs.text)
# print(company_list)

# print(company_list[0])


#list of company website
company_websites = []
for company in company_list:
    web_name = ''
    for char in company:
        if char == ' ':
            continue
        web_name += char.lower()
    company_websites.append('https://www.' + web_name + '.com')

# print(company_websites)


#  6. use request and enter into 100 webpages
no_of_companies = 0
for i in range(1, 100):
    try:
        company_website_login = requests.get(company_websites[i]).text
        no_of_companies += 1
        soup = BeautifulSoup(company_website_login, 'html.parser')
        print(no_of_companies * 10 )
        email = soup.find_all(string=re.compile('[a-zA-Z0-9]+@[a-z]+.[a-z]+'))
        if len(email) > 20:
            continue
        else:
            print(email)
        print('------------------------------------------------------------------------')
        if no_of_companies > 100:
            break
            
    except:
        print(company_websites[i] + 'error - unknown', type(company_websites[i]))
        no_of_companies -= 1


# data = """
# <a> sunny is a day </a>
# <a> sun is a star </a>
# <a> sunday is holiday </a>
# """

# search_word = 'sunny'
# soup = BeautifulSoup(data, 'html.parser')
# result = soup.find_all(string=re.compile('sun'))

# print(result)




    





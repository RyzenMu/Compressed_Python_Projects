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
import requests
from bs4 import BeautifulSoup


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

print(company_list[0])


#list of company website
company_website = []
for company in company_list:
    web_name = ''
    for char in company:
        if char == ' ':
            continue
        web_name += char.lower()
    company_website.append('www.' + web_name + '.com')

# print(company_website)



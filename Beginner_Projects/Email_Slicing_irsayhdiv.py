import requests

from bs4 import BeautifulSoup


vidhya_Page_1 = requests.get('https://www.google.com/search?q=linkedin+vidhyasri+ramalingam&client=ubuntu&channel=fs&ei=BUQjY7WoLOPw4-EPkMi6qA0&start=0&sa=N&ved=2ahUKEwj1vsHljZf6AhVj-DgGHRCkDtU4PBDy0wN6BAgBEDs&biw=1920&bih=968&dpr=1').text

vidhya_Page_2 = requests.get('https://www.google.com/search?q=linkedin+vidhyasri+ramalingam&client=ubuntu&channel=fs&ei=JUQjY7vsAfab4-EPuMW_yA4&start=10&sa=N&ved=2ahUKEwj7krj0jZf6AhX2zTgGHbjiD-kQ8tMDegQIARA8&biw=1920&bih=968&dpr=1').text

vidhya_Page_3 = requests.get('https://www.google.com/search?q=linkedin+vidhyasri+ramalingam&client=ubuntu&channel=fs&ei=-EgjY_UavZvj4Q-xnpHICA&start=20&sa=N&ved=2ahUKEwj19qjBkpf6AhW9zTgGHTFPBIk4ChDy0wN6BAgBED4&biw=1920&bih=968&dpr=1').text

vidhya_Page_4 = requests.get('https://www.google.com/search?q=linkedin+vidhyasri+ramalingam&client=ubuntu&channel=fs&ei=oUkjY-HrBbH7z7sPz-WQuAQ&start=30&sa=N&ved=2ahUKEwihwPmRk5f6AhWx_XMBHc8yBEc4FBDy0wN6BAgBEEA&biw=1920&bih=968&dpr=1').text

vidhya_Page_5 = requests.get('https://www.google.com/search?q=linkedin+vidhyasri+ramalingam&client=ubuntu&channel=fs&ei=u0kjY6OtGYPx4-EPoZay4AE&start=40&sa=N&ved=2ahUKEwjj9r-ek5f6AhWD-DgGHSGLDBw4HhDy0wN6BAgBEEI&biw=1920&bih=968&dpr=1').text

vidhya_list = [vidhya_Page_1, vidhya_Page_2, vidhya_Page_3, vidhya_Page_4, vidhya_Page_5]

for vidhya_element in vidhya_list:

    soup = BeautifulSoup(vidhya_element, 'lxml')

    vidhyas_in_page = soup.findAll('h3')

    for vidhya in vidhyas_in_page:
        print(vidhya.text)
        print('')



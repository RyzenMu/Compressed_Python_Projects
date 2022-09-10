# Create a contact book using json extension
# The contact book helps to add, modify and delete contacts using file handling



# Adding Contacts name to a file
# from unicodedata import name


# with open ('contacts-data/contacts_name.xls', 'w') as f:
#     f.write('Amgstrong\n')
#     f.write('Bruce\n')
#     f.write('Ceaser\n')
#     f.write('Doug Lyod\n')
#     f.write('Ethan Hunt\n')

# # Adding Contacts Phone number to a file
# with open ('contacts-data/contacts_numbers.xls', 'w') as f:
#     f.write('987654321\n')
#     f.write('976543218\n')
#     f.write('965432187\n')
#     f.write('954321876\n')
#     f.write('943218765\n')
    


# # Adding Contacts email to a file
# with open ('contacts-data/contacts_email.xls', 'w') as f:
#     f.write('amgstring@gmail.com\n')
#     f.write('bruce@gmail.com\n')
#     f.write('ceaser@gmail.com\n')
#     f.write('douglyod@gmail.com\n')
#     f.write('ethanhunt@gmail.com\n')


# # Creating a file object and reading the contents in it
# contacts_name_file = open('contacts-data/contacts_name.xls')
# print(contacts_name_file.readlines(200))

# # Once a file is opened it must be closed
# contacts_name_file.close()



condition = True

yes_or_no = input("Do You want to add a contact name to the existing contacts. Press Y or N : ")

while condition:
    if yes_or_no == 'y' or 'Y':
        name = input('Enter the Name : ')
        with open ('contacts-data/contacts_name.xls', 'a') as f:
            f.write(f'{name} \n')
        number = input('Enter the Phone Number : ')
        with open ('contacts-data/contacts_numbers.xls', 'a') as f:
            f.write(f'{number}\n')
        email = input('Enter the email : ')
        with open ('contacts-data/contacts_email.xls', 'a') as f:
            f.write(f'{email}\n')

        condition = False
    else:
        condition = False



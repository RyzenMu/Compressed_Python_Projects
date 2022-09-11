# Create a contact book using json extension
# The contact book helps to add, modify and delete contacts using file handling



# Adding Contacts name to a file
from unicodedata import name


with open ('contacts-data/contacts_name.xls', 'w') as f:
    f.write('Amgstrong\n')
    f.write('Bruce\n')
    f.write('Ceaser\n')
    f.write('Doug Lyod\n')
    f.write('Ethan Hunt\n')

# Adding Contacts Phone number to a file
with open ('contacts-data/contacts_numbers.xls', 'w') as f:
    f.write('987654321\n')
    f.write('976543218\n')
    f.write('965432187\n')
    f.write('954321876\n')
    f.write('943218765\n')
    


# Adding Contacts email to a file
with open ('contacts-data/contacts_email.xls', 'w') as f:
    f.write('amgstring@gmail.com\n')
    f.write('bruce@gmail.com\n')
    f.write('ceaser@gmail.com\n')
    f.write('douglyod@gmail.com\n')
    f.write('ethanhunt@gmail.com\n')


# Creating a file object and reading the contents in it
contacts_name_file = open('contacts-data/contacts_name.xls')
print(contacts_name_file.readlines(200))

# Once a file is opened it must be closed
contacts_name_file.close()




# add a contact
def add():
    yes_or_no = input("Do You want to add a contact name to the existing contacts. Press Y or N : ")


    if yes_or_no == 'y' or yes_or_no == 'Y':
        name = input('Enter the Name : ')
        with open ('contacts-data/contacts_name.xls', 'a') as f:
            f.write(f'{name} \n')
        number = input('Enter the Phone Number : ')
        with open ('contacts-data/contacts_numbers.xls', 'a') as f:
            f.write(f'{number}\n')
        email = input('Enter the email : ')
        with open ('contacts-data/contacts_email.xls', 'a') as f:
            f.write(f'{email}\n')

    else:
        print('OK Thank You!!!')


# modifying the existing file
def mod(name):
    yes_or_no = input("Do You want to Modify a contact name to the existing contacts. Press Y or N : ")

    if yes_or_no == 'y' or yes_or_no == 'Y':
   
        with open ('contacts-data/contacts_name.xls', 'r') as f:
            names_list = f.readlines()
            name = 'Bruce\n'
            for i in range(len(names_list)):
                if name == names_list[i]:
                    print(i)
                    new_name = input('Enter the New Name : ' )
                    names_list[i] = new_name + '\n'
                    with open ('contacts-data/contacts_name.xls', 'w') as w:
                        for name in names_list:
                            w.write(name)
                    break
        
        print(names_list)


        with open ('contacts-data/contacts_numbers.xls', 'r') as f:
            numbers_list = f.readlines()
            
            
            new_number = input('Enter the New Number : ')
            numbers_list[i] = new_number + '\n'
            with open ('contacts-data/contacts_numbers.xls', 'w') as w:
                for number in numbers_list:
                    w.write(number)
            
        
        print(numbers_list)


        with open ('contacts-data/contacts_email.xls', 'r') as f:
            email_list = f.readlines()
            
            
            new_email = input('Enter the New Email : ')
            email_list[i] = new_email + '\n'
            with open ('contacts-data/contacts_email.xls', 'w') as w:
                for email in email_list:
                    w.write(email)
            
        
        print(email_list)

    else:
        print('OK Thank You!!!')


def delete():
    pass






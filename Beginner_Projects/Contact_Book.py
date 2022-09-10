# Create a contact book using json extension
# The contact book helps to add, modify and delete contacts using file handling



# Adding Contacts to the file
with open ('contacts_name.xls', 'w') as f:
    f.write('Amgstrong\n')
    f.write('Bruce\n')
    f.write('Ceaser\n')
    f.write('Doug Lyod\n')
    f.write('Ethan Hunt\n')


with open ('contact_numbers.xls', 'w') as f:
    f.write('987654321\n')
    f.write('976543218\n')
    f.write('965432187\n')
    f.write('954321876\n')
    f.write('943218765\n')



with open ('contact_email.xls', 'w') as f:
    f.write('amgstring@gmail.com\n')
    f.write('bruce@gmail.com\n')
    f.write('ceaser@gmail.com\n')
    f.write('douglyod@gmail.com\n')
    f.write('ethanhunt@gmail.com\n')


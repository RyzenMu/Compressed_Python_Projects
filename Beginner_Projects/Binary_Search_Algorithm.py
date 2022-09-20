# Creating Data to search

import csv
import pandas as pd
import datetime
import string



# reading the csv file using pandas ans csv.Dict Reader
with open ('Beginner_Projects/data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        pass
        # print(row)


f = pd.read_csv('Beginner_Projects/data.csv')
first_name = f['first_name']
# print(first_name)

query_name='Orlan'

#normal searching i.e. linear search
print('_______________________________________ _______________________________')
start_time_linear_search = datetime.datetime.now()
print(f'starting time linear search :  {start_time_linear_search}')
for i in range(len(first_name)):
    if first_name[i] == query_name:
        print('Found')
end_time_linear_search = datetime.datetime.now()
print(f'ending time linear search :  {end_time_linear_search}')
print(f'duration : {(end_time_linear_search-start_time_linear_search)*10000}')
print('-----------------------------------------------------------------------')


#Binary searching i.e. linear search
start_time_Binary_search = datetime.datetime.now()
print(f'starting time Binary search :  {start_time_Binary_search}')
data = sorted(first_name)

middle = len(first_name)//2
middle_name = first_name[len(first_name)//2]
if query_name < middle_name:
    for i in range(0, middle, 1):
        if first_name[i] == query_name:
            print('found in first half', i)
else:
    for i in range(middle, len(first_name), 1):
        if first_name[i] == query_name:
            print('found in second half', i)


end_time_Binary_search = datetime.datetime.now()
print(f'ending time Binary search :  {end_time_Binary_search}')
print(f'duration : {(end_time_Binary_search-start_time_Binary_search)*10000}')
print('_______________________________________ _______________________________')




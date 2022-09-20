# Creating Data to search

import csv
import pandas as pd
import datetime



# reading the csv file using pandas ans csv.Dict Reader
with open ('Beginner_Projects/data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

f = pd.read_csv('Beginner_Projects/data.csv')
first_name = f['first_name']
print(first_name)

#normal searching i.e. linear search
start_time_linear_search = datetime.datetime.now()
print(f'starting time linear search :  {start_time_linear_search}')
for i in range(len(first_name)):
    if first_name[i] == 'Eulalie':
        print('found')
end_time_linear_search = datetime.datetime.now()
print(f'ending time linear search :  {end_time_linear_search}')
print(f'duration : {(end_time_linear_search-start_time_linear_search)*10000}')


#Binary searching i.e. linear search
start_time_Binary_search = datetime.datetime.now()
data = sorted(first_name)
print(data)
print(f'starting time Binary search :  {start_time_Binary_search}')
for i in range(len(first_name)):
    if first_name[i] == 'Eulalie':
        print('found')
end_time_Binary_search = datetime.datetime.now()
print(f'ending time Binary search :  {end_time_Binary_search}')
print(f'duration : {(end_time_Binary_search-start_time_Binary_search)*10000}')




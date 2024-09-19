'''
Michelle Zhu
Boas
SoftDev
K05 -- bitstream
2024-09-17
time spent: 0.5
'''

import random

data = open("krewes").read()
print(data)

'''
we want to make names the keys for the dictionary

1. split the string by person at @@@
2. split the fields at $$$
3.
'''

def parse_people_data(string):
    records = string.split('@@@') # step 1
    people_info = {} # dictionary {} to store the data
    
    for record in records:
        period, name, ducky = record.split('$$$') # stpe 2
        # store info using names as keys
        # !!! dictionary_name[key_name] = dictionary items
        people_info[name] = period, ducky
    return people_info
        
parse_people_data(data)

def get_info(name, people_info): # get info for selected person
    if name in people_info: # check if name is in dictionary
        period, ducky = people_info[name] # get period and ducky name for selected person
        print('Name: ' + name + '\n' + 'Period: ' + period + '\n' + 'Ducky: ' + ducky)
        
get_info('michelle', parse_people_data(data))


def random_get_info(people_info):
    # dict.keys() returns the keys of a dictionary
    # random.choice() only works with lists
    # convertion from dict to list needed
    # list(dict) converts dict to list
    random_name = random.choice(list(people_info.keys()))
    
    if random_name in people_info:
        period, ducky = people_info[random_name] # get period and ducky name for selected person
        print('Name: ' + random_name + '\n' + 'Period: ' + period + '\n' + 'Ducky: ' + ducky)
    
random_get_info(parse_people_data(data))
import time
import pandas as pd
import numpy as np
import calendar as cl
DATA_CITY = { 'All' : 'all',
              'Chicago': 'chicago.csv',
              'New york': 'new_york_city.csv',
              'Washington': 'washington.csv' }

DATA_Month = {
    0: 'All', 
    1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun',
    7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}

DATA_Day = ['All'] + [d[0:3] for d in cl.day_name]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    
    while True:
        msg = "Choose city:\n" \
        "[0]: All\n" \
        "[1]: Chicago\n" \
        "[2]: New York\n" \
        "[3]: Washington\n" \
        "Please type city name or number:"
        usrcity = "1" #input(msg)

        if usrcity.isnumeric() and int(usrcity) in range(len(DATA_CITY)) or usrcity.title() in DATA_CITY.keys():
            city = list(DATA_CITY.keys())[int(usrcity)] if usrcity.isnumeric() else usrcity.title() 
            break
        else:
            print("Wrong city Entry. :(")
        
        break #Remove this
    
    msg = "- You are choose {} {}.".format(city.title() if city.lower()!="all" else city.lower(),"city" if city.lower()!="all" else "cities")
    print(msg)
    
    # get user input for month (all, january, february, ... , june)

    while True:
        msg = "Choose month:\n" \
        "[0]: All\n" \
        "[?]: Month Number\n" \
        "Please type month name or number:"
        usrmonth = "1" #input(msg)

        if usrmonth.isnumeric() and int(usrmonth) in range(len(DATA_Month)) or usrmonth[:3].title() in DATA_Month.values():
            month = list(DATA_Month.values())[int(usrmonth)] if usrmonth.isnumeric() else usrmonth[:3].title() 
            break
        else:
            print("Wrong month Entry. :(")
        
        break #Remove this

    msg = "- You are choose {} {}.".format(month.lower(),"month" if month.lower() !="all" else "available monthes")
    print(msg)

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        msg = "Choose day:\n" \
        "[0]: All\n" \
        "[?]: Day Name\n" \
        "Please type week day name or number:"
        usrday = "1" #input(msg)

        if usrday.isnumeric() and int(usrday) in range(len(DATA_Day)) or usrday[:3].title() in DATA_Day:
            day = DATA_Day[int(usrday)] if usrday.isnumeric() else usrday[:3].title() 
            break
        else:
            print("Wrong day Entry. :(")
        
        break #Remove this

    msg = "- You are choose {}{}.".format(day.lower(),"day" if day.lower()!="all" else " available days")
    print(msg)

    
    print('-'*40)
    
    return city, month, day


print(type(get_filters()))

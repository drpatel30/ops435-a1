#!/usr/bin/env python3
'''OPS435 Assignment 1 - Fall 2019
Program: a1_drpatel30.py 
Author: "Dhyeykumar Patel"
The python code in this file (a1_drpatel30.py) is original work written by
"Dhyeykumar Patel". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''

import sys
import os

############################################################################
#Usage function 
############################################################################

def usage():
    '''usage() will check the number of arguments and if it has too few 
    it will return usage
    usage() 
    Usage: ./a1_drpatel30.py [--step] YYYY/MM/DD +/-n
    (END)
    '''
    if len(sys.argv) != 4 or len(sys.argv) != 3:
        print('Usage:',sys.argv[0],'[--step] YYYY/MM/DD +/-n')

#############################################################################
# Checking the number of arguments and storing the values in correct
# variables 
#############################################################################

if len(sys.argv) == 4:
    if len(sys.argv[2]) == 10:
        date1=sys.argv[2]
        str_year, str_month, str_date=date1.split('/')
        year=int(str_year)
        month=int(str_month)
        date=int(str_date)
        days=int(sys.argv[3])
        step=True
    else:
	    print("Error: wrong date entered")
	    sys.exit()
elif len(sys.argv) == 3:
    if len(sys.argv[1]) == 10:
        date1=sys.argv[1]
        str_year, str_month, str_date=date1.split('/')
        year=int(str_year)
        month=int(str_month)
        date=int(str_date)
        days=int(sys.argv[2])
    else:
	    print("Error: wrong date entered")
	    sys.exit()
else:
    usage()    

##########################################################################
#Valid_date function 
##########################################################################

def valid_date():
    '''
    valid date function checks if the correct values for date, month
    is entered and correct format is followed and gives appropriate 
    error message:
    i.e. 
    wrong days entered is more than 31 , "Error:wrong day entered"
    wrong month entered is more than 12,  "Error:wrong month entered"
    wrong date is entered : "Error: wrong date entered "
    (END)
    '''
    if len(sys.argv) == 4:
        if date <= 31 and month <= 12 and len(sys.argv[2]) == 10:
            return 'true'
        else:
            if date > 31:
                a= "Error: wrong day entered"
            elif month > 12:
                a= "Error: wrong month entered"
            elif len(sys.argv[2]) != 10:
                a= "Error: wrong date entered "
            return a 
    elif len(sys.argv) == 3:
        if date <= 31 and month <= 12 and len(sys.argv[1]) == 10:
            return 'true'
        else:
            if date > 31:
                a= "Error: wrong day entered"
            elif month > 12:
                a= "Error: wrong month entered"
            elif len(sys.argv[1]) != 10:
                a= "Error: wrong date entered "
            return a
    else:
        usage()

##########################################################################
#leap year function 
##########################################################################

def leap_year():
    '''
    leap year function does not take any arguments and
    dertermines if a year in argument given is a 
    leap year or not and returns True or Flase value
    (END)
    '''
    if valid_date() == 'true':
        if (year % 400) == 0 or (year%100 !=0 and year%4==0) :
	        return True
        else:
            return False
    else:
        return valid_date()

##########################################################################
#days_in_month function 
##########################################################################

def days_in_month(month):
    '''
    the functino returns maximum number of days in a month
    when a month is entered as an argument in integer format.
    (END)
    ''' 
    if valid_date() == 'true':
        if leap_year():
            feb_max=29
        else:
            feb_max=28
        mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        days_m=mon_max[month]
        return days_m

##########################################################################
#after function 
##########################################################################

def after(today):
    '''
    after(today) -> str
    after() takes a valid date string in 'YYYY/MM/DD' format and return a 
    date string for the next day in 'YYYY/MM/DD' format.
    e.g. after('2017/12/31') -> '2018/01/01'
         after('2018/01/31') -> '2018/02/01'
         after('2018/02/28') -> '2018/03/01'
    (END) 
    '''
    if valid_date() == 'true':
        date_1=today
        str_year, str_month, str_date=date_1.split('/')
        year_1=int(str_year)
        month_1=int(str_month)
        date_1=int(str_date)
        temp_date= date_1 + 1
        if temp_date > days_in_month(month_1):
            temp_date = 1
            temp_month = month_1+1
            temp_year=year_1
            if temp_month > 12: 
                temp_month = 1
                temp_year=year_1 +1
        else:
            temp_month=month_1
            temp_year=year_1 
        next_day=str(temp_year).zfill(4)+'/'+str(temp_month).zfill(2)+'/'+str(temp_date).zfill(2)
        return next_day
    else:
        return valid_date()

##########################################################################
#before function 
##########################################################################
          
def before(today):
    '''
    before(today) -> str
    before() takes a valid date string in 'YYYY/MM/DD' format and return a 
    date string for the previous day in 'YYYY/MM/DD' format.
    e.g. before('2018/01/01') -> '2017/12/31'
         before('2018/02/01') -> '2018/01/31'
         before('2018/03/01') -> '2018/02/28'
    (END) 
    '''
    if valid_date() == 'true':
        date2=today
        str_year, str_month, str_date=date2.split('/')
        year_2=int(str_year)
        month_2=int(str_month)
        date_2=int(str_date)
        temp_date2= date_2 - 1
        if temp_date2 == 0 :
            temp_month2 = month_2 - 1
            if temp_month2 == 0: 
                temp_month2 = 12
                temp_year2=year_2 - 1
            else:
                temp_year2=year_2
            temp_date2=days_in_month(temp_month2)
        else:
            temp_month2=month_2
            temp_year2=year_2 
        previous_day=str(temp_year2).zfill(4)+'/'+str(temp_month2).zfill(2)+'/'+str(temp_date2).zfill(2)
        return previous_day
    else:
        return valid_date()

##########################################################################
#dbda function 
##########################################################################

def dbda(z, days):
    '''
    dbda(date,days) -> str
    dbda function takes two arguments and returns a string depending 
    on the argument given as days(n).
    if days are positive it will call after function and return date 
    after n days.
    e.g. dbda(2019/01/01,3) -> '2019/01/03'
    if days are negetive it will call before function and return date 
    before n days.
    e.g. dbda(2019/01/03,3) -> '2019/01/01'
    '''
    if len(sys.argv) == 3:
        if int(days)>= 0:
            for x in range(int(days)):
                z=after(z)
            return z
        if int(days) < 0:
            for x in range(abs(int(days))):
                z=before(z)
            return z
    elif  len(sys.argv) == 4:
        if int(days) >= 0:
            for x in range(int(days)):
                z=after(z)
                print(z)
        if int(days) < 0:
            for x in range(abs(int(days))):
                z=before(z)
                print(z)	
    
##########################################################################
#main executable code  
##########################################################################

if __name__ == "__main__":
    if len(sys.argv) == 3: 
        print(dbda(sys.argv[1],sys.argv[2]))
    elif (len(sys.argv)==4 and sys.argv[1]== '--step'):
        dbda(sys.argv[2],sys.argv[3])   
    

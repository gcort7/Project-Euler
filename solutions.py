# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:38:50 2019

@author: Gio
"""
from dateutil.relativedelta import relativedelta
from useful_functions import isPrime, checkPrimes_substrs, get_permutation, replace_letters
import datetime as dt
import pandas as pd 
import math
#%% Exercise 16: 
def exercise_16(x):
    suma = 0 
    for i in str(x): 
        suma += int(i)
    return suma

print('The answer is: ', exercise_16(2**1000))

#%% Exercise 19: 

def exercise_19(ini_date, end_date):
    
    count_sunday = 0 
    
    paridad_weekdays = {0: 'Monday', 
                        1: 'Tuesday', 
                        2: 'Wednesday', 
                        3: 'Thurday', 
                        4: 'Friday', 
                        5: 'Saturday', 
                        6: 'Sunday'}
    
    centuries = [i for i in range(0, end_date.year + 100, 100)]
    
    paridad_months_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 
                           7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    
    id_day = ini_date.day
    numberofyears = end_date.year - ini_date.year + 1
    
    for year in range(1, numberofyears + 1):
        if year != numberofyears: numberofmonths = 12 
        else: numberofmonths = end_date.month
        if (ini_date + relativedelta(years = year - 1)).year % 4 == 0:
            paridad_months_days[2] = 29
            if ((ini_date + relativedelta(years = year - 1)).year in centuries 
            and (ini_date + relativedelta(years = year - 1)).year % 400 != 0): 
                paridad_months_days[2] = 28
        else: paridad_months_days[2] = 28
        for month in range(1, numberofmonths + 1):
            id_day = id_day + paridad_months_days[month] % 7
            if id_day > 6: id_day -= 7
            if paridad_weekdays[id_day] == 'Sunday': count_sunday += 1
    
    return count_sunday  

ini_date = dt.datetime(1901, 1, 1)
end_date = dt.datetime(2000, 12, 31)
print('The answer is: ', exercise_19(ini_date, end_date))

#%% Exercise 22:

def exercise_22(f_path):
    strings = open(f_path, "r")
    text = strings.read()
    lista = text.split(",")
    names_org = pd.DataFrame(lista)
    
    names_org = names_org.sort_values(by = 
                names_org.columns.tolist()[0]).reset_index(drop = True)
    
    names_org['sum'] = names_org[names_org.columns.tolist()[0]].apply(lambda x: 
                                                            replace_letters(x))
    names_org['pos'] = [i for i in range(1, len(names_org) + 1)]
    names_org['result'] = names_org['sum'] * names_org['pos']
    
    return names_org['result'].sum()

f_path = r'C:\Users\Gio\Desktop\Project-Euler\files\p022_names.txt'
print('The answer is: ', exercise_22(f_path))

#%% Exercise 24: 
permutations = get_permutation('0123456789')
print('The answer is: ', permutations[999999])

#%% Exercise 37: 
def exercise_37(criteria): 
    select_primes, exception, number = [], [2, 3, 5, 7], 1
    while len(select_primes) < criteria:
        print(number)
        if isPrime(number) and (number not in exception):
            if (checkPrimes_substrs(str(number), 'right') and 
                checkPrimes_substrs(str(number), 'left')):
                select_primes.append(number)
        number += 1
    return sum(select_primes)

print('The answer is: ', exercise_37(11))

#%% Exercise 57: 
def exercise_57(criteria):
    cont, div, criteria = 0, 10, 1001
    for i in range(1, criteria):
        if i == 1:
            a, b, c = 2, 1, 2
        else:
            if len(num) > 2:
                b_, c = c/div, a*c/div + b/div
                b = b_
            else:
                b_, c = c, a*c + b
                b = b_
                num, den = c + b, c 
        num, den = str(math.floor(c + b)), str(math.floor(c))
        if len(num) > len(den): cont += 1
    
    return cont
    
print('The answer is: ', exercise_57(1001))






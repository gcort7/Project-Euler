# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:38:50 2019

@author: Gio
"""

from useful_functions import isPrime, checkPrimes_substrs, get_permutation
import math
#%% Exercise 24: 
permutations = get_permutation('0123456789')
print('The answer is: ', permutations[999999])

#%% Exercise 37: 
select_primes, exception, number, criteria = [], [2, 3, 5, 7], 1, 11
while len(select_primes) < criteria:
    print(number)
    if isPrime(number) and (number not in exception):
        if (checkPrimes_substrs(str(number), 'right') and 
            checkPrimes_substrs(str(number), 'left')):
            select_primes.append(number)
    number += 1
print('The answer is: ', sum(select_primes))
#%% Exercise 57: 
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
    
print('The answer is: ', cont)






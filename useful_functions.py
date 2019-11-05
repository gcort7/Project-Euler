# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:36:31 2019

@author: Gio
"""


def isPrime(n) : 
    
    # Return True if the number is prime 
    # otherwise return False. 
    
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

    
def checkPrimes_substrs(string, order): 
    
    # break down a string into substrings (from left to right and 
    # vice versa) and check those are primes. 
    
    if len(string) > 0: 
        if isPrime(int(string)) == True:
            if order == 'right': return checkPrimes_substrs(string[1:], order)
            else: return checkPrimes_substrs(string[:-1], order)
        else: return False
    return True

def get_permutation(string):
    
    # This function return all permutations from the string inserted
    
    permutations = []
    if len(string) == 1:
        permutations.append(string)
        return permutations
    
    for post in range(0, len(string)):
        innerpermutations = get_permutation(string[0:post] + string[post + 1:])
        for str_ in range(0, len(innerpermutations)):
            permutations.append(string[post] + innerpermutations[str_])
    return permutations


def replace_letters(letter):
    
    # This function adds all the numbers corresponding to the string
    paridad_alphabet = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 
                        'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14,'O':15, 
                        'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 
                        'W':23, 'X':24, 'Y':25, 'Z':26}

    suma = 0
    for l in letter:
        try: suma += paridad_alphabet[l]
        except: print('letter was not found')
    return(suma)


# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 02:43:33 2021

@author: pratikgl
"""


# amount of money
m = 40 

# array of dem=nominations
c = [25, 10, 5, 1]

# number of denominations
d = 4

# BRUTEFORCECHANGE(M, c, d)

no_of_coins = 999999999 #infinity
final = [0, 0, 0, 0]
the_range = [m//c[0], m//c[1], m//c[2], m//c[3]] 
big = [[0, 0, 0, 0]]
k = 1

def Valueofcoins(arr):
    lola = 0
    for i in range(4):
        lola = lola + c[i]*arr[i]
    return lola

for i in range(d):
    j = the_range[i]
    while(j > 0):
        for index in range(k):
            pp = list(big[index])
            pp[i] = j
            big.append(pp)
            
            # check for every pp
            if Valueofcoins(pp) == m:
                temp = pp[0]+pp[1]+pp[2]+pp[3]
                if no_of_coins > temp:
                    no_of_coins = temp
                    final = pp
            
        j -= 1
    k = len(big)

# the final result
for i in range(d):
    print('coin of denomination ', end='')
    print(c[i], end='')
    print(' => Number of coins = ', end='')
    print(final[i])

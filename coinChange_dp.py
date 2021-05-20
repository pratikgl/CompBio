# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 12:53:33 2021

@author: pratikgl
"""

# amount of money
m = 40

# array of dem=nominations
c = [25, 10, 5, 1]

# number of denominations
d = 4

# dynamic_programming(M, c, d)

# initialising the array with infinity
inf = 999999999
dp = [inf]*(m+5)
final = [[0, 0, 0, 0]]*(m+5)

dp[0] = 0 # base condition

for i in range(1, m+1):
    for j in range(d):
        if(c[j]<=i and dp[i-c[j]] + 1 < dp[i]):
                dp[i]=dp[i-c[j]] + 1
                final[i] = final[i-c[j]].copy()
                final[i][j] += 1
                
# the final result
for i in range(d):
    print('coin of denomination ', end='')
    print(c[i], end='')
    print(' => Number of coins = ', end='')
    print(final[m][i])

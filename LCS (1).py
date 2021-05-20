# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 21:35:42 2021

@author: pratikgl
"""

"""
Write a dynamic programming algorithm to compute longest common sub-sequence between two strings
Considering the examples discussed in the class
seq1 = ATCTGAT
seq2 = TGCATA
LCA = TCTA (final solution)
note here that TGAT is also a valid solution
"""

def LCS(x, y):
    
    dp = [[0]*(len(y)+5)]
    for _ in range(len(x)+5):
        dp.append([0]*(len(y)+5))
    
    for i in range(len(x)+1):
        for j in range(len(y)+1):
            if(i==0 or j==0):
                continue
            elif (x[i-1]==y[j-1]):
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j], dp[i][j-1])
            
    m = len(x)
    n = len(y)
    
    last = dp[m][n]
    lcs = ''; i=m; j=n
    while(i and j):
        if(x[i-1]==y[j-1]):
            lcs = x[i-1]+lcs
            i-=1; j-=1; last-=1
        elif (dp[i-1][j]<dp[i][j-1]):
            j-=1
        else:
            i-=1
            
    return lcs


seq1 = 'ATCTGAT'
seq2 = 'TGCATA'

print('The LCS of ' + seq1 + ' and ' + seq2 +' is :')
print(LCS(seq1, seq2))
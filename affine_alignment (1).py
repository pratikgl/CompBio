# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:37:56 2021

@author: pratikgl
"""
"""
Global alignment using affine gap penalties
"""

seq1 = 'AGGCTACTTTCA'
seq2 = 'GGCTACTATATCA'

m = len(seq1)  #12
n = len(seq2)  #13

dp = []
gap = []
for _ in range(n+1):
        dp.append([0]*(m+1))
        gap.append([0]*(m+1))

gap_init = -5
gap_extend = -1
mismatch = -1
match = 1

# matrix filling dynamic programming method

dp[0][1]=gap_init
dp[1][0]=gap_init

for i in range(2, m+1):
    dp[0][i]=dp[0][i-1]+gap_extend
for i in range(2, n+1):
    dp[i][0]=dp[i-1][0]+gap_extend

for i in range(1, 1+n):
    for j in range(1, 1+m):
        score=0
        if(seq1[j-1]==seq2[i-1]):
            score=match
        else:
            score=mismatch
        
        gap1 = gap_init
        if(i>=2 and dp[i-2][j]+gap_init==dp[i-1][j]):
            gap1 = gap_extend
            
        gap2 = gap_init
        if(j>=2 and dp[i][j-2]+gap_init==dp[i][j-1]):
            gap2 = gap_extend
            
        dp[i][j]=max(dp[i-1][j-1]+score,
                     dp[i-1][j]+gap1, 
                     dp[i][j-1]+gap2)

seq1_align = ''
seq2_align = ''

i=n
j=m
count=0
# backtracking algorithm
while(i!=0 or j!=0):
    count+=1
    flag=0
    if((flag!=1) and i>0):
        gap1 = gap_init
        if(i>=2 and dp[i-2][j]+gap_init==dp[i-1][j]):
            gap1 = gap_extend
        if(dp[i-1][j]+gap1 == dp[i][j]):
            seq1_align =  '-' + seq1_align
            seq2_align = seq2[i-1] + seq2_align
            i=i-1
            flag=1
        
    if((flag!=1) and j>0):
        gap2 = gap_init
        if(j>=2 and dp[i][j-2]+gap_init==dp[i][j-1]):
            gap2 = gap_extend
        if(dp[i][j-1]+gap2 == dp[i][j]):
            seq1_align =  seq1[j-1]+seq1_align
            seq2_align =  '-'+seq2_align
            j = j-1
            flag=1
            
    if((flag!=1) and j>0 and i>0):
        if(seq1[j-1]==seq2[i-1] or dp[i-1][j-1] + mismatch == dp[i][j]):
            seq1_align =  seq1[j-1]+seq1_align
            seq2_align =  seq2[i-1]+seq2_align
            i=i-1
            j=j-1
            flag=1

print(seq1_align)
print(seq2_align)
print("The score of the optimal alignment is: " + str(dp[n][m]))

"""
Final output of the code:

AGGCTACTTT--CA
-GGCTACTATATCA
The score of the optimal alignment is: -2
"""







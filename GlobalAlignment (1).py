# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 12:29:56 2021

@author: pratikgl
"""

seq1 = 'AGGCTACTTTCA'
seq2 = 'GGCTACTATATCA'
#seq1 = 'AGC'
#seq2 = 'AAAC'
m = len(seq1)  #12
n = len(seq2)  #13

dp = []
for _ in range(n+1):
        dp.append([0]*(m+1))

gap_penalty = -2
mismatch = -1
match = 1

# matrix filling dynamic programming method

for i in range(1, m+1):
    dp[0][i]=dp[0][i-1]+gap_penalty
for i in range(1, n+1):
    dp[i][0]=dp[i-1][0]+gap_penalty

for i in range(1, 1+n):
    for j in range(1, 1+m):
        score=0
        if(seq1[j-1]==seq2[i-1]):
            score=match
        else:
            score=mismatch
        dp[i][j]=max(dp[i-1][j-1]+score,
                     dp[i-1][j]+gap_penalty, 
                     dp[i][j-1]+gap_penalty)

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
        if(dp[i-1][j]+gap_penalty == dp[i][j]):
            seq1_align =  '-' + seq1_align
            seq2_align = seq2[i-1] + seq2_align
            i=i-1
            flag=1
            
    if((flag!=1) and j>0):
        if(dp[i][j-1]+gap_penalty == dp[i][j]):
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

AGGCTACT-T-TCA
-GGCTACTATATCA
The score of the optimal alignment is: 5
"""







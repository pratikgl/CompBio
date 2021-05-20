# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 16:04:43 2021

@author: pratikgl
"""

# Dynamic Programming algorithm to solve the manhattan tourist problem

# Description of the problem
"""
Matrix dimension => 5*5
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


# representation of a 2-d matrix

adj = [[11, 12, 13, 14, 15], 
       [21, 22, 23, 24, 25],
       [31, 32, 33, 34, 35],
       [41, 42, 43, 44, 45],
       [51, 52, 53, 54, 55]]

# dictionary representation of weights on the edges
weight = {
    '11->12' : 3,
    '12->13' : 2,
    '13->14' : 4,
    '14->15' : 0,
    '11->21' : 1,
    '12->22' : 0,
    '13->23' : 2,
    '14->24' : 4,
    '15->25' : 3,
    
    '21->22' : 3,
    '22->23' : 2,
    '23->24' : 4,
    '24->25' : 2,
    '21->31' : 4,
    '22->32' : 6,
    '23->33' : 5,
    '24->34' : 2,
    '25->35' : 1,
    
    '31->32' : 0,
    '32->33' : 7,
    '33->34' : 3,
    '34->35' : 4,
    '31->41' : 4,
    '32->42' : 4,
    '33->43' : 5,
    '34->44' : 2,
    '35->45' : 1,
    
    '41->42' : 3,
    '42->43' : 3,
    '43->44' : 0,
    '44->45' : 2,
    '41->51' : 5,
    '42->52' : 6,
    '43->53' : 8,
    '44->54' : 5,
    '45->55' : 3,
    
    '51->52' : 1,
    '52->53' : 3,
    '53->54' : 2,
    '54->55' : 2
    }

dp = [[0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0]]

# for the first row and first col
for i in range(2, 6):
    s = '1' + str(i-1) + '->' + '1' + str(i)
    dp[1][i] = max(dp[1][i], dp[1][i-1] + weight[s])
    
    s = str(i-1) + '1' + '->' + str(i) + '1'
    dp[i][1] = max(dp[i][1], dp[i-1][1] + weight[s])
    

# dynamic programming algorithm for the rest of the nodes
for i in range(1, 6):
    for j in range(1, 6):
        if(i-1 != 0):
            s = str(i-1)+str(j) + '->' + str(i)+str(j)
            dp[i][j] = max(dp[i][j], dp[i-1][j]+weight[s])
        
        if(j-1 != 0):
            s = str(i)+str(j-1) + '->' + str(i)+str(j)
            dp[i][j] = max(dp[i][j], dp[i][j-1]+weight[s])

# printing the final score
# X and Y are the coordinates of the sink
X = 5
Y = 5
print('The final score to the destination is: ' + str(dp[X][Y]))

# printing the matrix final score:
print('\nThe matrix final scores for all the nodes are:')
for i in range(1, 6):
    for j in range(1, 6):
        print(dp[i][j], end='\t')
    print()
    

# backtracking to find the path
path=[[0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0]]

m = 5
n = 5
path[m-1][n-1] = 1
final_path = [[m-1, n-1]]
while(m!=1 or n!=1):
    if(n-1>0):
        s = str(m)+str(n-1) + '->' + str(m)+str(n)
        if(dp[m][n]==dp[m][n-1]+weight[s]):
            path[m-1][n-2]=1
            final_path.append([m-1,n-2])
            n-=1
        else:
            path[m-2][n-1] = 1
            final_path.append([m-2, n-1])
            m-=1
    else:
        path[m-2][n-1] = 1
        final_path.append([m-2, n-1])
        m-=1
        
# plotting the graph
fig = plt.figure(figsize=(7, 7))
fig.suptitle('Dynamic Programming solution for Manhattan tourist problem')
ax = plt.axes()

count = 1
for row in range(5):
    for col in range(5):
        
        plt.subplot(5, 5, count)
        count=count+1
        plt.xticks([])
        plt.yticks([])
        
        if [row,col] in final_path:
            plt.text(0.5, 0.5, str(dp[row+1][col+1]), ha='center', va='center', 
                     size=40, backgroundcolor='palegreen')
            
        else:
            plt.text(0.5, 0.5, str(dp[row+1][col+1]), ha='center', va='center', 
                     size=40, backgroundcolor='darkgrey', color='white')

plt.show()


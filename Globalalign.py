# Given in the question

X = 'CAGCTAGCG'
Y = 'CCATACGA'

# penalty score (given in the question)
GAP = -1
MM = -1
PM = 1


# initialising the matrix with zero score
dp = []
for i in range(len(Y)+1):
    temp = []
    for j in range(len(X)+1):
        temp.append(0)
    dp.append(temp)


# matrix filling dynamic programming method

# initliasing the first row using the gap values
for i in range(len(X)):
    dp[0][i+1] = dp[0][i]+GAP
    
# initalising the first column values using the gap values
for i in range(len(Y)):
    dp[i+1][0] = dp[i][0]+GAP


# filling of the dp matrix using the global alignment algorithm
for i in range(len(Y)):
    for j in range(len(X)):
        
        # considering the case of pair match
        if(X[j]==Y[i]):
            dp[i+1][j+1]=max(dp[i][j]+PM,dp[i][j+1]+GAP, dp[i+1][j]+GAP)
        
        # conisdering the case of mis match
        else:
            dp[i+1][j+1]=max(dp[i][j]+MM,dp[i][j+1]+GAP, dp[i+1][j]+GAP)
        

# the final aligned sequence
X_align = ''
Y_align = ''

# the length of the both of the sequences needed for the backtracking algorithm
i = len(Y)
j = len(X)


# backtracking algorithm for global alignment to get the final sequece aligned
while(True):
    if(i > 0 and dp[i-1][j] + GAP == dp[i][j]):
        X_align =  '-' + X_align
        Y_align = Y[i-1] + Y_align
        i-=1
            
    elif(j > 0 and dp[i][j-1] + GAP == dp[i][j]):
       # if():
        X_align =  X[j-1] + X_align
        Y_align =  '-' + Y_align
        j-=1
            
    else:
        X_align =  X[j-1]+X_align
        Y_align =  Y[i-1]+Y_align
        i-=1 
        j-=1
    if(i==0 and j==0):
        break
    
# printing the final result
print("Score of the alignment -> " + str(dp[len(Y)][len(X)]))
print('\nThe algined sequence is: ')    
print(X_align)
print(Y_align)


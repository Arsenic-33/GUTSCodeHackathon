# We have N cream puffs.

# Find all possible number of people to which we can evenly distribute the cream puffs without cutting them.

# Input Format
# N

# Output Format
# Print the numbers (as an integer) of people in ascending order, each as a new line.


#Failed 1 Test Case 9.6/10

from math import sqrt
N=int(input())
x=sqrt(N)
y=int(x)
factors=[1,N]
if(x==y):
    for i in range (2,y):
        if(N%i==0):
            factors.append(i)
            factors.append(N//i)
    factors.append(y)
else:
    for i in range (2,y+1):
        if(N%i==0):
            factors.append(i)
            factors.append(N//i)
         
        
factors.sort()
for x in factors:
    print(x)
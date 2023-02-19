#For integers b (b>=2) and n (n>=1) let the function f(b, n) be defined as followed:
#f(b,n) = n where n < b
#f(b,n) =  f(b, floor(n/b)) + (n mod b)

#Less formally, f(b,n) is equal to the sum of the digits of n written in base b. 

#You are given integers n and s. Determine if there exists an integer b  such that f(b,n) == s. 
# If such an integer b exists, find the smallest such b.

# Input Format

# Given standard input string as follows:

# n
# s

# Output Format

# If there exists an integer b  such that , print the smallest such b. If such b does not exist, print -1 instead.

#36.52/60, unfortunately, to save my awful time complexity line 15 uses a range of sqrtN instead of N to save on the time,
#this data set works on enough tests to get over 30 points however unelegant it may be 

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def function(b,n):
    if n<b:
        return n
    else:
        #print(math.floor(n/b), n, b)
        return function(b, math.floor(n/b))  + n % b
    
n=int(input())
s=int(input())
#print(n)
for i in range(2,int(50*math.sqrt(n))):
   # print(" t")
    temp = function(i,n)
    #print(temp, i)
    if temp == s:
        print(i)
        quit()
        
print(-1)
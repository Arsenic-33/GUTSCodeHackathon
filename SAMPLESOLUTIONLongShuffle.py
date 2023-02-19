# MASSIVE DISCLAIMER
# THIS IS NOT MY CODE, I DID NOT UPLOAD THIS, NOT CLAIM IT AS MY OWN
# THIS IS SIMPLY AS EVERYONE FOUND THIS QUESTION AWFULLY HARD AND AFTER THE HACKATHON WE FOUND A SOLUTION FROM A JAPANESE HACKATHON

#Problem Statement
# There is an array 
# A1 ,…,An and initially Ai = i for all  i. Define the following routine shuffle(L,R):

# If  R=L+1, swap values of AL and AR and terminate.
# Otherwise, run 
# shuffle(L,R−1) followed by 
# shuffle(L+1,R).
# Suppose we run 
# shuffle(1,N). Print the value of 
# AK
# ​after the routine finishes.

# For each input file, solve 
# T test cases.

# Constraints
# 1≤T≤1000
# 2≤N≤10^18
# 1≤K≤N
# Input
# The input is given from Standard Input in the following format:
# T
# case1
# ​case2
# ​⋮
# caseT
 
# Each case is in the following format:
# N 
# K


# Output
# Print T lines. The i-th line should contain the answer for the i-th case.



def ans(n,k,bit):
  b=1<<bit
  if n&b==0: return ans(n,k,bit-1)
  if n==b:
    if k%2==0: return k-1
    else: return k+1
  elif n==b+1:
    if k==1: return 2
    elif k==n-1: return n
    elif k%2==1: return k-2
    else: return k+2
  else:
    if k<=n-b: return ans(n-b,k,bit-1)
    elif k>=b+1: return ans(n-b,k-b,bit-1)+b
    else: return k
    
T=int(input())
for _ in range(T):
  N,K=map(int,input().split())
  print(ans(N,K,60))
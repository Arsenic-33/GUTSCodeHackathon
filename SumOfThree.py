# You are given two integers K and S.

# The three variables X, Y, and Z are integer values satisfying 0 ≤ X, Y, Z ≤ K.

# How many different assignments of values to X, Y, and Z are there such that X + Y + Z = S?

# Input Format
# A single string parameter to your function in the form:
# K   S

#Output format
#Number of valid XYZ triplets as an integer

#20/20

nums = [eval(i) for i in input().split(" ")]

K = nums[0] 
S = nums[1]
rt=0
for i in range(K+1):
    for j in range(K+1):
        x = S-i-j
        if x>=0 and x <= K:
            rt+=1

print(rt)
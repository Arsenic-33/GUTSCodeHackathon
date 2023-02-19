# Florence has N integers, Her objective is to have N equal integers by transforming some of them.

# She may transform each integer at most once. Transforming an integer X into another integer Y costs her (x-y)^2 pounds. Even if ai = aj, she has to pay the cost separately for transforming each of them (see Sample 2).

# Find the minimum total cost to achieve her objective.

# Input Format

# Given standard input string as follows:

# N
# a1,a2,a3,...,an

#30/30

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
lis =  [eval(i) for i in input().split(" ")]

avg = round (sum(lis)/len(lis))
rt = 0
for i in range(len(lis)):
    rt += (avg-lis[i])**2
    
print(int(rt))


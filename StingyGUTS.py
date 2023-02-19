# Welcome to a low budget DYHTG. T-shirts are only given to participants according to the following rules.

# All participants who ranked Ath or higher get a T-shirt. Additionally, from the participants who ranked between (A+1)th and Bth (inclusive), C participants chosen uniformly at random get a T-shirt.

# There were 1000 participants in this contest, and all of them got different ranks. DominicJina, who participated in this contest, ranked Xth. Find the probability that they get a T-shirt.

# Input Format

# A B C X

#Output Format
#Print the answer as a float. Your output will be considered correct if the absolute or relative error from the given answer is at most 10^−12.

#30/30

# Enter your code here. Read input from STDIN. Print output to STDOUT

lis = input().split(" ")

nums = [eval(i) for i in lis]

participant = nums[3]

if participant > nums[1]:
    print(0)
elif participant <= nums[0]:
    print(1)
else:
    print( nums[2]/(nums[1]-nums[0]) )


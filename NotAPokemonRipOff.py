# Mahnoor is into a game where you keep pets.

# Mahnoor's pet is Euan. Initially, Euan's STR is X and EXP is 0. These parameters increase in the following two kinds of training:

# Go to Stevie Gym: the STR gets multiplied by A, and the EXP increases by 1.
# Go to Bank Street Bar: the STR increases by B, and the EXP increases by 1.
# Euan evolves when his STR becomes Y or greater, but Mahnoor thinks that makes him less cute.

# Find the maximum possible EXP of Euan when he is trained without letting him evolve.

# Input Format
# Given as standard input:
# X Y A B

# Output Format
# Print the maximum possible EXP of Euan under the given situation as an integer.

#This solution kinda blows, very slow, just brute force really, 22.76/30 all timeout errors, very easy to optimise to make them all work but this isnt a charity :)

# Enter your code here. Read input from STDIN. Print output to STDOUT
nums = [eval(i) for i in input().split(" ")]
X = nums[0] #Init str
Y = nums[1] #Max STR
A = nums[2] #Multiply
B = nums[3] #Add
EXP = 0

while X<Y:
    if X*A < X+B:
        X= X*A
        EXP+=1
    else:
        X=X+B
        EXP+=1

print(EXP-1)
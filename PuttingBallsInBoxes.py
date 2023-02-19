# We have removed A balls from a box that contained N balls and then put B new balls into that box. 
# How many balls does the box contain now?

# Input Format
# Given as standard input in a single line:
# N  A  B

# Constraints
# All values in input are integers.

# Output Format
# X

# Print an integer equal to the number of balls in the end.


# This can obviously be done better, I did this in 15 seconds 10/10
inp = input()
Values = inp.split(" ")
print(int(Values[0]) - int(Values[1]) + int(Values[2]))
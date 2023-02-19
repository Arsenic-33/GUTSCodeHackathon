
# You are given a string S. Find the lexicographically smallest string S' obtained by permuting the characters of S.

# Here, for different two strings s=s1s2…sn and t=t1t2…tm,  holds lexicographically when one of the conditions below is satisfied.

# There is an integer i  such that sii and sj = tj for all integers j . si = ti for all integers i , and .

# Input Format

# Given as a standard input string

# S
# Constraints

# S is a string of length between 1 and 2×105 (inclusive) consisting of lowercase English letters.

# Output Format

# Print the lexicographically smallest string S′ obtained by permuting the characters in S.

#Magically easy  40/40

print( "".join( sorted([*input()]) ))
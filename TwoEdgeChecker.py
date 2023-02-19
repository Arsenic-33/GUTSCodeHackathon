#Image of Tree https://s3.amazonaws.com/hr-assets/0/1676385084-4bdb31cd85-080021a4ef4143f82d024ce3b4cfd00f.png

#Determine if there is a segment that directly connects the points numbered a and b in the figure below.

#Input Format
#Given as a single string input as:
#a b

#Output Format
#Print the string "Yes" if there is a segment that directly connects the points numbered a and b; print the string "No" otherwise.

#20/20

lis = input().split(" ")
nums = [eval(i) for i in lis]
if nums[1] // nums[0] == 2:
    print("Yes")
else:
    print("No")
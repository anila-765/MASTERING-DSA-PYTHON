'''
Prob 2: Write a program to check whether a triangle can be formed with the given values for the angles.

If sum of angles is equal to 180, then triangle can be formed, else it can't be formed.

Input: 45 45 45

Expected Output: 

Triangle cannot be formed

Explanation -> We are getting 3 inputs, that is three angles of triangle, but here the sum of three angles that is 45+45+45 is not equal to 180 so Triangle cannot be formed is the output.
'''
n1=int(input())
n2=int(input())
n3=int(input())
s=n1+n2+n3
if s==180:
    print("Triangle ca be formed")
else:
    print("triangle  cannot be formed")

'''
Write a Program to find the power of a number recursively. Take two inputs, number and the power.

Example:
Input: 2 3

Output: 8

Explanation : 2^3 is 8

Example:

Input: 5 2

Output: 25

Explanation: 5^2 is 25

Solution is available in the github repo but do solve it on your own.
'''
n=int(input("enter a base "))
p=int(input("enter power "))
def power(n,p,i=1):
    if i>p:
        return 1
    else:
        return n*power(n,p,i+1)
    
   
print(power(n,p))
        

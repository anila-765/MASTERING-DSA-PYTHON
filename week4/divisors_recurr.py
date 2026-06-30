'''
Write a program to print the divisors of a number recursively.

Example:
Input: 6

Output: 1 2 3 6



Example:

Input: 12

Output: 1 2 3 4 6 12
'''
n=int(input("enter a number "))

def div(n,i=1):
    if i>n:
        return 
    if n%i==0:
        print(i,end=" ")
    
    return div(n,i+1)
div(n)
        

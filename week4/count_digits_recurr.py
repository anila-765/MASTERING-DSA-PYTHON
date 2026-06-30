'''
Write a recursive algorithm to find the count of digits in a number.

Example:
Input: 353445

Outpput: 6

Example 2 :

Input: 53543

Output: 5
'''
n=int(input("enter a number "))

def count(n):
    if n%10==n:
        return 1
    else:
        return 1 + count(n//10)
print(count(n))
        

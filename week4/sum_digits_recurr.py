'''
Write a recursive program to find the sum of digits of a number.

Example:

Input: 342

Output: 9



Example 2:
Input: 34534

Ouput: 19
'''
n=int(input("enter a number "))

def sum_dig(n):
    if n%10==n:
        return n
    else:
        return n%10 + sum_dig(n//10)
print(f"sum of digits = {sum_dig(n)}")
        

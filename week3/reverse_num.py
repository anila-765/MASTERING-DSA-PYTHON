'''
Write a program that gets n as input and print the reverse of the number

Testcase 1 :

Input : 

325345

Expected output:


543523



Testcase 2 :

Input : 

987987

Expected output:

789789
'''
n=int(input("Enter a number"))
rev=0
while n>0:
    ld=n%10
    rev=rev*10+ld
    n=n//10
print(f"reversed number {rev}")

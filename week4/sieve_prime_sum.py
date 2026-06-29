'''
Given a range [L, R]. The task is to find the sum of all the prime numbers in the given range
from L to R both inclusive.

Input : L = 10, R = 20
Output : Sum = 60
Prime numbers between [10, 20] are:
11, 13, 17, 19
Therefore, sum = 11 + 13 + 17 + 19 = 60
Input : L = 15, R = 25
Output : Sum = 59

Note: Use sieve of eratosthenes to solve the problem

O/P=>
length50
l=10
R=20
[11, 13, 17, 19]
sum=  60
'''

n=int(input("length"))
l = int(input("l="))
r  = int(input("R="))
arr = [1]*(n+1)
for i in range(2,int(n**.5)+1):
            if arr[i] == 1:
                for j in range(i*2,n+1,i):
                    arr[j] = 0
                   
arr2 = []
sum_ = 0
for i in range(l,r+1):
            if arr[i]==1:
                arr2.append(i)
                sum_+=i
print(arr2)
print("sum= ",sum_)

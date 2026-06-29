'''
Sieve of Eratosthenes
Difficulty: MediumAccuracy: 47.43%Submissions: 78K+Points: 4
Given a positive integer n, calculate and return all primes less than or equal to n using the 
Sieve of Eratosthenes algorithm.

Examples:

Input: n = 10
Output: [2, 3, 5, 7]
Explanation: Prime numbers less than equal to 10 are 2, 3, 5 and 7.
'''
class Solution:
    def sieve(self, n):
        # code here 
        arr = [1]*(n+1)
        for i in range(2,int(n**.5)+1):
            if arr[i] == 1:
                for j in range(i*2,n+1,i):
                    arr[j] = 0
                   
        arr2 = []
        for i in range(2,n+1):
            if arr[i]==1:
                arr2.append(i)
        return arr2

'''
Find the n-th Fibonacci number for a given non-negative integer n.
The Fibonacci sequence is defined as:

F(0) = 0
F(1) = 1
F(n) = F(n - 1) + F(n - 2) for n ≥ 2
Examples :

Input: n = 5
Output: 5
Explanation: The 5th Fibonacci number is 5.
'''
class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        if n==1:
            return 1
        elif n==0:
            return 0
        else:
            return self.nthFibonacci(n-1)+self.nthFibonacci(n-2)

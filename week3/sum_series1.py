#Given a number n, find the nth term in the series 1, 3, 6, 10, 15, 21…
class Solution:
    def findNthTerm(self, n):
        # code here 
        return n*(n+1)//2

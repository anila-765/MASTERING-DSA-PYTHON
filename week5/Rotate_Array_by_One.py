'''
Given an array arr, rotate the array by one position in clockwise direction.

Examples:

Input: arr[] = [1, 2, 3, 4, 5]
Output: [5, 1, 2, 3, 4]
'''
class Solution:
    def rotate(self, a):
        n=len(a)
        temp=a[n-1]
        
        for i in range(n-1,0,-1):
            a[i]=a[i-1]
        a[0]=temp
    

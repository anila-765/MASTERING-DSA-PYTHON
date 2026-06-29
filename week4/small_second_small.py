'''
Given an array, arr[] of integers, your task is to return the smallest and second smallest element in the array.
If the smallest and second smallest do not exist, return -1.

Examples:

Input: arr[] = [2, 4, 3, 5, 6]
Output: [2, 3] 
Explanation: 2 and 3 are respectively the smallest and second smallest elements in the array
'''
class Solution:
    def minAnd2ndMin(self, arr):
        # code here
        small = arr[0]
        l = len(arr)
        for i in range(l):
            if small > arr[i]:
                small = arr[i]
        s2 = float('inf')
        for i in range(l):
            if arr[i] > small:
                if arr[i] < s2:
                    s2 = arr[i]
                
            
        if s2 == float("inf"):
            return [-1]
        else:
            
            return [small,s2]
       

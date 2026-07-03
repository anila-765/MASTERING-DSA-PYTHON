'''
Given an array of positive integers arr[], return the second largest element from the array. 
If the second largest element doesn't exist then return -1.
'''
class Solution:
    def getSecondLargest(self, arr):
        # code here
        large = arr[0]
        
        for i in arr:
            if i>large:
                large=i
        sl=-1
        for i in arr:
            if i>sl and i!=large:
                sl=i
        return sl

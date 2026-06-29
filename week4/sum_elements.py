'''
Given an integer array arr[], return the sum of all elements of arr.

Examples:

Input: arr[] = [1, 2, 3, 4]
Output: 10
Explanation: 1 + 2 + 3 + 4 = 10.
'''
class Solution:
	def arraySum(self, arr):
   		# code here
        sum_num = 0
        
        for i in arr:
            sum_num += i
        return sum_num

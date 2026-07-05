'''
Remove Duplicates Sorted Array
Difficulty: EasyAccuracy: 38.18%Submissions: 385K+Points: 2Average Time: 20m
You are given a sorted array arr[] containing positive integers. 
Your task is to remove all duplicate elements from this array such that each element appears only once. 
Return an array containing these distinct elements in the same order as they appeared.
Examples :

Input: arr[] = [2, 2, 2, 2, 2]
Output: [2]
Explanation: After removing all the duplicates only one instance of 2 will remain i.e. 
[2] so modified array will contains 2 at first position and you should return array containing [2] 
after modifying the array.
'''



Custom Input
class Solution:
    def removeDuplicates(self, arr):
        # code here 
        n=len(arr)
        j=0
        b=[]
        for i in range(n-1):
            if arr[i]!=arr[i+1]:
                b.append(arr[i])
                j+=1
        b.append(arr[n-1])
        return b

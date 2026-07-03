'''
Dutch National Flag Algorithm

The Dutch National Flag Algorithm is used to sort an array containing only 0s, 1s, and 2s in one traversal.

Idea
'''
class Solution:
    def sort012(self, a):
        # code here
        left=0
        mid=0
        right=len(a)-1
        
        while mid<=right:
            if a[mid]==1:
                mid+=1
            elif a[mid]==0:
                a[left],a[mid]=a[mid],a[left]
                mid+=1
                left+=1
            elif a[mid]==2:
                a[mid],a[right]=a[right],a[mid]
                right-=1
            

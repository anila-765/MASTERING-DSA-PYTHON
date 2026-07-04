
'''
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

'''

class Solution:
    def intersection(self, a: List[int], b: List[int]) -> List[int]:
        n=len(a)
        m=len(b)
        k=0
        res=[]
        for i in range(n):
            for j in range(m):
                flag = 1
                if a[i]==b[j]:
                    for h in range(k):
                        if a[i]==res[h]:
                            flag=0
                            break
                    if flag==1:
                        res.append(a[i])
                        k+=1
        return res

'''
nput: a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
Output: [1, 2, 3]
'''
class Solution:    
    def findUnion(self, a, b):
        # code here
        def unionArray(a,res,k):
            m=len(a)
            n=len(res)
            for i in range(m):
                flag=0
                for j in range(k):
                    if a[i]==res[j]:
                        flag=1
                        break
                if flag==0:
                    res.append(a[i])
                    k+=1
            return k
            
        
        k=0
        res=[]
        k=unionArray(a,res,k)
        k=unionArray(b,res,k)
        return res

class Solution:
    def reverseString(self, s: str) -> str:
        # code here
        ls=list(s)
        n=len(ls)
        i=0
        j=n-1
        while i<=j:
            ls[i],ls[j]=ls[j],ls[i]
            i+=1
            j-=1
        s="".join(ls)#space complexity=O(n)
        return s
    

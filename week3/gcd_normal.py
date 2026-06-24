class Solution:
    def gcd(self, a, b):
        # code here
        if a<b:
            n=a
        else:
            n=b
        gcd=1
        for i in range(2,n+1):
            if(a%i==0 and b%i==0):
                gcd=i
                
        return gcd

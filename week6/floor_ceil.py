class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # code here
  
        
        def floor1(x:int,arr:list)->list:
            n=len(arr)
            i=0
            j=n-1
            if arr[i]>x:
                return -1
            while i<=j:
                mid=(i+j)//2
                if arr[mid]==x:
                    return arr[mid]
                elif arr[mid]<x:
                    i=mid+1
                else:
                    j=mid-1
            return arr[j]
        def ceil1(x:int,arr:list)->list:
            i=0
            n=len(arr)
            j=n-1
            if arr[j]<x:
                return -1
            while i<=j:
                mid=(i+j)//2
                if arr[mid]==x:
                    return arr[mid]
                elif arr[mid]<x:
                    i=mid+1
                else:
                    j=mid-1
            return arr[i]
            
        arr.sort()
        flor= floor1(x,arr)
        cil = ceil1(x,arr)
        
        return [flor,cil]

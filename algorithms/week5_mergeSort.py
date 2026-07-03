
def mergeSort(l,h,a):
    if l<h:
        mid = (l+h)//2
        mergeSort(l,mid,a)
        mergeSort(mid+1,h,a)
        merge(l,mid,h,a)
        
def merge(l,mid,h,a):
   
    b=[]
    c=[]
    for x in range (l,mid+1):
        b.append(a[x])
    for x in range(mid+1,h+1):
        c.append(a[x])
    k=l
    i=0
    j=0
    n = len(b)
    m = len(c)
    while(i<n and j<m):
        if b[i]<=c[j]:
            a[k]=b[i]
            i+=1
            k+=1
        else:
            a[k]=c[j]
            j+=1
            k+=1
    while(i<n):
        a[k]=b[i]
        i+=1
        k+=1
    while(j<m):
        a[k]=c[j]
        j+=1
        k+=1
a = [5,6,1,4,12,16]
n=len(a)-1
mergeSort(0,n,a)
print(a)
    
         

'''
4
  *
 ***
*****
 ***
  *
'''
n=int(input())
ncpy=n
n=n-1
for i in range(1,n+1):
    for j in range(1,(n-i)+1):
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("*",end="")
    print()
n=ncpy-2
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" ",end="")
    for j in range(1,((2*n)-(2*i-1))+1):
        print("*",end="")
    print()
  


        
        

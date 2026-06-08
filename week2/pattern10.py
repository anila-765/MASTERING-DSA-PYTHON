'''
Input: n = 4 
Output:
    *
   ***
  *****
 *******

'''
n = int(input())

# code here
for i in range(1,n+1):
    for j in range(1,(n-i)+1):
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("*",end="")
    for j in range(1,(n-i)+1):
        print(" ",end="")    
    print()

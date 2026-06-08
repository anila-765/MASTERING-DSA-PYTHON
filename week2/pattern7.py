'''
4=>input
4321
321
21
1

'''
n=int(input())

for i in range(1,n+1):
    for j in range(n-i+1,0,-1):
        print(j,end="")
    print()
  


        
        

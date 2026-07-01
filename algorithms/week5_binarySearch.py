'''
algorithm
a = [1,3,8,28,42,43,99,101,102] #sorted array
x=int(input("enter search element)")
low = 0
high = len(a)-1
while low<= high:
    mid = (low+high)//2
    if a[mid] == x:
        return mid:
    elif a[mid] < x:
        low = mid+1
    else:
        low = mid-1
return -1
'''

def binary_search(a, x):
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] == x:
            return mid
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1


a = [1, 3, 8, 28, 42, 43, 99, 101, 102]

x = int(input("Enter search element: "))

result = binary_search(a, x)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

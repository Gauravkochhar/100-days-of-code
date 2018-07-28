# Python program for implementation of heap Sort


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


n=int(input("Enter the number of nodes in the Tree:"))
arr=[]
for i in range(n):
    print(i+1,"->",end='')
    el=int(input())
    arr.append(el)

heapSort(arr)
n = len(arr)
print("\n\n**********************************************",end='\n')
print("Sorted array is :",end='\n')
for i in range(n):
    if i==n-1:
        print(arr[i],"",end='\n')
    else:
        print(arr[i],",",end='')
print("**********************************************",end='\n')

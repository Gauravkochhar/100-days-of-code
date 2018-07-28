/* Program to Write Merge two Arrays and then apply Merge sort Algorithm to sort the elements of merged array. */


n1=int(input("Enter the number of element for array 1:"))
n2=int(input("Enter the number of element for array 2:"))
arr1=[]
arr2=[]
arr3=[]
print("\nEnter the elements of Array1:",end='\n')
for i in range(n1):
    print(i+1,"->",end=' ')
    el=int(input())
    arr1.append(el)
print("\nEnter the elements of Array2:",end='\n')
for i in range(n2):
    print(i+1,"->",end=' ')
    el=int(input())
    arr2.append(el)
totalelement=n1+n2
print("\nNow Merge Operation is performing......",end='\n')
k=0
for i in range(totalelement):
    if(i<=4):
        el=arr1[i]
        arr3.append(el)
    else:
        el=arr2[k]
        k=k+1
        arr3.append(el)
print("Now the Merged Array is:")
print("[",end='')
for i in range(totalelement):
    if i==totalelement-1:
        print(arr3[i],"",end=' ')
    else:
        print(arr3[i], ",", end=' ')
print("]")

for i in range(totalelement):
    for j in range(i+1,totalelement):
        if(arr3[j]<arr3[i]):
            temp=arr3[j]
            arr3[j]=arr3[i]
            arr3[i]=temp
print("\n\n\n**********************************************",end='\n')
print("Now The Sorted Elements are:")
for i in range(totalelement):
    if i==totalelement-1:
        print(arr3[i],"",end='')
    else:
        print(arr3[i], ",", end='')
print("\n**********************************************")

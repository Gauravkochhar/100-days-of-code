print("Enter the Number of elements:")
n=int(input())
a=[]
for i in range(n):
    print("Enter ",i+1,"th element is:")
    val=input()
    a.append(int(val))
print("Old Values Are:")
print(a,end='\n')
lengthArr=len(a)
for i in range(lengthArr-1):
    swap=0
    for j in range(lengthArr-i-1):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            swap=1
    if(swap == 0):
        break
print("\n\n*************************************************")
print("Now the Sorted Elements are in Python:")
print(a)
print("*************************************************")


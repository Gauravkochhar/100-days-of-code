n=int(input("Enter the Number of Element to be Sorted:"))
a=[]
for i in range(n):
    print("Enter ",i+1,"th Element:")
    val=int(input())
    a.append(val)
print("Old Values are:")
print(a)
lengthArr=len(a)
for i in range(lengthArr-1):
    min=a[i]
    loc=i
    for j in range(i+1,lengthArr):
        if(a[j]<min):
            min=a[j]
            loc=j
    temp=a[i]
    a[i]=a[loc]
    a[loc]=temp

print("\n\n**************************************")
print("Now the Sorted Elements are:")
print(a)
print("**************************************")

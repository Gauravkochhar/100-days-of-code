n=int(input("Enter the number to be Sorted:"))
a=[]
for i in range(n):
    print("Enter ",i+1,"th Element:")
    val=int(input())
    a.append(val)
print("Old Values Are:")
print(a)
lengthArr=len(a)
for i in range(1,lengthArr):
    temp=a[i]
    j=i-1
    while(j>=0 and a[j]>temp):
        a[j+1]=a[j]
        j=j-1
    a[j+1]=temp
print("\n\n****************************************")
print("Now the Sorted Elements are:")
print(a)
print("*****************************************")

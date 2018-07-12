print("Enter the Number of elements:",end=' ')
n=int(input())
a=[]
for i in range(n):
    print("Enter ",i+1,"--->:",end=' ')
    val=int(input())
    a.append(val)
lengthArr=len(a)
for i in range(1,lengthArr):
    temp=a[i]
    j=i-1
    while(j>=0 and a[j]>temp):
        a[j+1]=a[j]
        j=j-1
    a[j+1]=temp

print("Sorted form of Entered Elements are :")
print(a)

min=[]
if(a[0]!=0):
    smallestMis=0
    min.append(smallestMis)
else:
    l=len(a)
    for i in range(0,l-1):
        if(a[i+1]-a[i]>1):
            b=list(range(a[i]+1,a[i+1]))
            smallestMis=a[i]+1
            min.append(smallestMis)
listOfMissing=len(min)
if(a[0]==0 and listOfMissing==0):
    print("\n\n**********************************************")
    print("There is no Missing element in the series")
    print("***********************************************")
else:
    minimum=min[0]
    for i in range(listOfMissing-1):
        if(min[i]<minimum):
            minimum=a[i]
    print("\n\n**********************************************")
    print("Smallest Missing element in the array is:",end=' ')
    print(minimum)
    print("***********************************************")

def binarySearch(a,se,n,low,high):
    mid=int((low+high)/2)
    if(se==a[mid]):
        print("***************************************************")
        print("Element Search is successful,element is exist.")
        print("***************************************************")
        return True
    elif(se>a[mid]):
        low=mid+1
        return binarySearch(a,se,n,low,high)
    elif(se<a[mid]):
        high=mid-1
        return binarySearch(a,se,n,low,high)
    else:
        print("***************************************************")
        print("Entered Element is not exists in the Array elements.")
        print("***************************************************")
        return False
n=int(input("Enter the number of element:"))
a=[]
low=0
high=n
print("Enter the elements in the sorted form:",end='\n')
for i in range(n):
    print(i + 1, "th element is: ",end=' ')
    e=int(input())
    a.append(e)
print("Entered elements are:",end=' ')
for i in range(n):
    print(a[i],end=' ')
se=int(input("\nEnter the element you want to search:"))
binarySearch(a,se,n,low,high)

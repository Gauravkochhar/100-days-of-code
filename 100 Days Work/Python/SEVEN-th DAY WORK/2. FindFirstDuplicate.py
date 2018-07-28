n=int(input("Enter the number of element in the Array:"))
a=[]
for i in range(n):
    print(i+1,"->",end=' ')
    el=int(input())
    a.append(el)
print("Entered Eleements are:",end='\n')
for i in range(n):
    if i==n-1:
        print(a[i],"",end='')
    else:
        print(a[i],",", end=' ')
for i in range(n):
    count=0
    d=0
    for j in range(n):
        if(a[i]==a[j]):
            count=count+1
            if (count > 1):
                print("\n\n***************************************************")
                print("First Duplicate element in the Array is: ", a[i])
                print("***************************************************")
                d=d+1
                break

    if(d>0):
        break

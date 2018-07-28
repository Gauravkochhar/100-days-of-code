n=int(input("Enter the number of Elements:"))
a=[]
for i in range(n):
    print(i+1,"th->",end=' ')
    el=int(input())
    a.append(el)
print("Elements you inserted are:")
print("{ ",end='')
for i in range(n):
    if i==n-1:
        print(a[i],"",end='')
    else:
        print(a[i], ",", end=' ')
print("}")
print("ALL THE PAIRS WHOSE ELEMENT-SUM IS ZERO",end='\n')
for i in range(n):
    count = 0
    for j in range(n):
        if(a[i]+a[j]==0):
            print("[",end='')
            print(a[i],",",a[j],end='')
            print("]")
            count=count+1
    if(count == 0 and i==n-1):
        print("*******************************************************")
        print("There are no elements in the array whose sum is zero")
        print("*******************************************************")

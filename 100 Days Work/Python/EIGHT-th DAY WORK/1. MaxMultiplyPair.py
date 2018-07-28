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
a1=a[0]
b1=a[1]
for i in range(n):
    for j in range(i+1,n):
        if(a[i]*a[j]>a1*b1):
            a1=a[i]
            b1=a[j]
print("\n\n****************************************",end='\n')
print("Max Mutiply pair is:",end="\n")
print("[",a1,",",b1,"]",end='\n')
print("****************************************")

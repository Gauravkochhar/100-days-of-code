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
duplicate=[]
for i in range(n):
    count=0
    for j in range(n):
        if(a[i]==a[j]):
            count=count+1
            if (count > 1):
                if a[i] in duplicate:
                    print("")
                else:
                    duplicate.append(a[i])
len=len(duplicate)
print("\n\n***************************************")
print("Duplicate ELements are:",end='\n')
print("[",end='')
for i in range(len):
    if i==len-1:
        print(duplicate[i],end='')
    else:
        print(duplicate[i],",",end='')
print("]",end='\n')
print("***************************************")


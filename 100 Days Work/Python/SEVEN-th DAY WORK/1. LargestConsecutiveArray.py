n=int(input("Enter the number of element in the array:"))
a=[]
largestConsecutive=[]
for i in range(n):
    print(i+1,"->",end=' ')
    el=int(input())
    a.append(el)

print("Entered Elements are:",end='\n')
print("{",end='')
for i in range(n):
    if i==n-1:
        print(a[i], end='')
    else:
        print(a[i],",",end='')
print("}")
for i in range(n):
    if(a[i]+1==a[i+1]):
        largestConsecutive.append(a[i])
    else:
        largestConsecutive.append(a[i])
        break
print("\n\n*******************************************")
print("Largest Consecutive Array is:",end='\n')
len=len(largestConsecutive)
print("[",end='')
for i in range(len):
    if i==len-1:
        print(largestConsecutive[i],end='')
    else:
        print(largestConsecutive[i], ",", end='')
print("]")
print("*******************************************")

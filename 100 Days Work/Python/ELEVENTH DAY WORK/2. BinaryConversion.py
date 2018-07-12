print("Binary Digit Of :",end=' ')
n=int(input())

a=[]
while n>=1:
    rem=n%2
    i = 0
    a.append(rem)
    n=int(n/2)
    i=i+1
print("is=",end='')
l=len(a)
for i in reversed(a):
    print(i,end='')

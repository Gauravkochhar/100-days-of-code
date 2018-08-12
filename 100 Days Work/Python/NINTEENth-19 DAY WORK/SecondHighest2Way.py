
n=int(input())
arr=list(map(int, input().split()))
r=Remove(arr)
m1=r[0]
m2=r[1]
if(m2>m1):
    m1,m2=m2,m1
for i in r[2:len(r)]:
    if(i>m2):
        if(i>m1):
            m2=m1
            m1=i
        else:
            m2=i
print("*********************************")
print("Second Larges value is:",m2)
print("**********************************")

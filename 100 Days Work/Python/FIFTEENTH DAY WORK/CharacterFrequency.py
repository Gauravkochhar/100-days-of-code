s=input("Enter a string:")
j=0
print("********************************************")
print("{  ",end='')
for i in range(97,123):
    count=0
    for j in range(len(s)):
        if(chr(i)==s[j]):
            count=count+1
    if(count>0):
        print(chr(i),":",count,end='  ')
print("}")
print("********************************************")

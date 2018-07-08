str=input("Enter a String:")
b=''
for x in range(1,len(str)+1):
    b=b+str[-x]
str=b
print("Now The Reverse String is :",b)

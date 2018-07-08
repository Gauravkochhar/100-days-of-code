num1=int(input("Enter First number:"))
num2=int(input("Enter Second number"))
a=num1
b=num2

while(b!=0):
    temp=b
    b=a%b
    a=temp
print("HCF of ",num1,"and ",num2,"is:",a)
a=int(((num1*num2)/a))
print("LCM of ",num1,"and",num2,"is:",a)

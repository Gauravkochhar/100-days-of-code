#Write a Python program to compute the sum of the two reversed numbers and display the sum in reversed form.

n1=int(input("Enter first Number"))
n2=int(input("Enter second Number"))

#Now reversing process will be start
rem=1
rev=0
rev1=0
rev2=0
while(n1>0):
    rem=n1%10
    rev=10*rev+rem
    n1=int(n1/10)
print(rev)

while(n2>0):
    rem=n2%10
    rev1=rev1*10+rem
    n2=int(n2/10)
print(rev1)

sum=rev+rev1
while(sum>0):
    rem=sum%10
    rev2=rev2*10+rem
    sum=int(sum/10)
print("After reversing sum is :",rev2)

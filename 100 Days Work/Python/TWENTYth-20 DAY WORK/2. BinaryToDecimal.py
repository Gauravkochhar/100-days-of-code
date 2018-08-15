n=int(input("Enter a binary number to get Decimal Number: " ))
base=1
dv=0
while(n>0):
    rem=n%10
    dv=dv+rem*base
    n=int(n/10)
    base=base*2
print("Decimal Number is: ",dv)

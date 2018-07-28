?*
1. Reverse the bits of a given integer by using binary operators.
   This problem is a bit basic problem and need to dig a bit deeper. So, you guys are free to write program in
   C or C++ as well.

Input :
    -100 has binary representation as '11111111111111111111111110011100'
      On reversing bits, it should be '00111001111111111111111111111111'              */

    
    
n=input("Enter a nunber:")
nlength=len(n)
a = []
if(n[0]=='-'):
    val = 1
    num = int(n[1:nlength])
    n = num
    while n > 0:
        rem = n % 2
        n = int(n / 2)
        a.append(rem)
    a.append(val)
    print("\n\n*************************************************")
    print("Binary Number is               :   ", end=' ')
    for i in reversed(a):
        print(i, end='')
    print("")
    print("Reverse of the Binary Number is:   ", end=' ')
    len = len(a)
    for i in range(len):
        print(a[i],end='')
    print("\n*************************************************")

elif(n[0]=='+'):
    val = 0
    num = int(n[1:nlength])
    n = num
    while n > 0:
        rem = n % 2
        n = int(n / 2)
        a.append(rem)
    a.append(val)
    print("\n\n*************************************************")
    print("Binary Number is               :   ", end=' ')
    for i in reversed(a):
        print(i, end='')
    print("")
    print("Reverse of the Binary Number is:   ", end=' ')
    len = len(a)
    for i in range(len):
        print(a[i], end='')
    print("\n*************************************************")

else:
    val = 0
    num = int(n[:nlength])
    n = num
    while n > 0:
        rem = n % 2
        n = int(n / 2)
        a.append(rem)
    a.append(val)
    print("\n\n*************************************************")
    print("Binary Number is               :   ", end=' ')
    for i in reversed(a):
        print(i, end='')
    print("")
    print("Reverse of the Binary Number is:   ",end=' ')
    len =len(a)
    for i in range(len):
        print(a[i], end='')
    print("\n*************************************************")

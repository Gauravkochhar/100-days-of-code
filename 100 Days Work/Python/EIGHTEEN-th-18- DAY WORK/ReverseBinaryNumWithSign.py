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

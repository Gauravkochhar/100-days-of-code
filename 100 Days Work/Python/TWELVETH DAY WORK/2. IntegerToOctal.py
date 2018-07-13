print("Enter a Number:",end=' ')
n=input()
a=[]
if(n[0]=='-'):
    print("\n\nNot Possible For Negative Number")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")
else:
    if(n[0]=='+'):
        n=int(n[1:len(n)])
        while n>0:
            rem=n%8
            n=int(n/8)
            a.append(rem)
    else:
        n = int(n[0:len(n)])
        while n > 0:
            rem = n%8
            n =int(n/8)
            a.append(rem)
    print("\n\n************************************")
    print("Octal number is: ", end='')
    for i in reversed(a):
        print(i, end='')
    print("")
    print("************************************")

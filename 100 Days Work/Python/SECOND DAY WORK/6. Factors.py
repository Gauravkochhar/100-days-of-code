num=int(input("Enter a number to find a factors:"))
print("\n\nNow the Factors of the Numbers are :")
for i in range(1,num+1):
   
    if(i == 1 and num%i == 0 ):
        print("(",i, end="\t,")

    if(i!=1 and i!=num and num%i == 0):
        print(i,end="\t,")

    if(num%i == 0 and i == num):
        print(i, end="\t)")


num1=int(input('Enter the first Number:'))
num2=int(input('Enter the Second Number:'))

print('Enter the Operation you want among +,-,*,/')
op=input()

if(op == '+'):
    print(num1+num2)
elif(op == '*'):
    print(num1*num2)
elif(op == '/'):
    print(num1/num2)
elif(op == '-'):
    print(num1-num2)
else:
    print("Entered Function is not Working due to Lower version or invalid Function")

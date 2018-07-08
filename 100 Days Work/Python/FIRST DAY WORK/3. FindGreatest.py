x = int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))
z = int(input("Enter the value of z:"))
if x > y and x > z:
    print('x is greater than y and z')
elif y > x and y > z:
    print('y is greater than x and z')
else:
    print('z is greater than x and y')

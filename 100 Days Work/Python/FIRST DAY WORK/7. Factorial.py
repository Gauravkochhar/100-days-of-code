num = 5
factorial = 1
if num < 0:
    print('Sorry ,There is no factorial for negative number')
elif num == 0:
    print('factorial zero value is 1')
else:
    for i in range(1 , num + 1):
        factorial = factorial*i
    print('factorial of',num,' is ',factorial)

count = 0
l=int(input('Enter the Lower limit:'))
h=int(input('Enter the higher limit:'))
for j in range(l, h + 1 ):
    for i in range(1,j + 1):
        if j%i == 0:
            count=count+1
    if count > 2:
        count = 0
    else:
        print('',j)
        count = 0

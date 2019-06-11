First way

import numpy as np
values=[1,2,3]
arr = np.array(values,'i')
print(arr)


Second Way

from array import array
arr = array('i',[1,2,3])
print(arr[0])


Third Way

from array import array
n= int(input("Enter number of element :"))
a=[]
for i in range(1,n+1):
    a.append(i)
arr = array('f',a)
for i in range(len(arr)):
    print(arr[i])

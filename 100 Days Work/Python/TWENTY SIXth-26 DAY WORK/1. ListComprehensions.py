"""
Sample Input 0
1
1
1
2

Sample Output 0
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

"""

x=int(input("Enter 1st:"))
y=int(input("Enter 2nd: "))
z=int(input("Enter 3rd: "))
n=int(input("Enter the value of n="))
result=[]
s=0
finalresult=[]
for k in range(x+1):
    for j in range(y+1):
        for i in range(z+1):
            if(k<=x and j<=y and i<=z ):
                if(k+j+i!=n):
                    finalresult.append([])
                    finalresult[s].append(k)
                    finalresult[s].append(j)
                    finalresult[s].append(i)
                    s=s+1
print(finalresult)

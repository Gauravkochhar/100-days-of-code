
n=int(input("Enter the number of element of the list:"))
ls=[]
for i in range(n):
    print("Enter ",i+1,"th element:")
    e=int(input())
    ls.append(e)
print(ls)
print("Total elements are without , are")
rs=" ".join(str(i) for i in ls)
print(rs)

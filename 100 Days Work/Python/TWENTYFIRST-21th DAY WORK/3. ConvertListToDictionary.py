n=int(input("Enter the number of the student of the physics in a class:"))
list=[]
for i in range(n):
    list.append([])
    n = input("name")
    g = float(input("grade"))
    list[i].append(n)
    list[i].append(g)
print(list)
d={}
for (key,value) in list:
    d[key]=value
print(d)    

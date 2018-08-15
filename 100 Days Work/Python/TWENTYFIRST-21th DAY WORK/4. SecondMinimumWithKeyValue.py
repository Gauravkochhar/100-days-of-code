list=[["gaurav",34],["raghav",45],["Suchit",45],["Akhil",56]]

d={}
for (key,value) in list:
    d[key]=value
print(d)
min=float("inf")
minName=""
for i,v in d.items():
    if(v<min):
        min=v
        minName=i
secondMin=float("inf")
secondMinName=""
secondMinList=[]
i=0
for key,value in d.items():
    if(value>min and value<=secondMin):
        secondMin=value
        secondMinName=key
        secondMinList.append([])
        secondMinList[i].append(secondMin)
        secondMinList[i].append(secondMinName)
        i=i+1
print(secondMinList)



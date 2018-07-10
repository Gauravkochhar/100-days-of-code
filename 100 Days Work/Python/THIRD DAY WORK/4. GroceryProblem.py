d={"Flour":10,"Rice":10,"Sugar":5,"Pulse 1":2,"Pulse 2":2,"Pulse 3":2}
with open('Groslist.txt','a')as wf:
    for itm,qunt in d.items():
        print(itm)
        print(qunt)
        word= itm + " => " + str(qunt) +"Kg\n"
        wf.write(word)

print("----------------------------------------------------------------")
item=input("Enter the Item you want to Search:")
quantity=d[item]
print("Available Quantity is: ",quantity)

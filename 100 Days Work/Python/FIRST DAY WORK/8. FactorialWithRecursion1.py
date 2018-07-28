def function(n):
    fact = 1
    if(n==0):
        return 1
    else:
        return n*function(n-1)

num=int(input("Enter a number to find a factorial:"))
result=function(num)
print("The factorial of:",num," is:",result)

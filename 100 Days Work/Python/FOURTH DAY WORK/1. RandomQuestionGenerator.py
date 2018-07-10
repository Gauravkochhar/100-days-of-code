import random
def myfun():
    num1=random.randint(100,999)
    num2=random.randint(1,99)
    print("The Sum of ",num1," and ",num2," is:")
    sum=int(input())
    if num1+num2 != sum:
        print("you answered Incorrect.")
    else:
        print("you answered Correct.")
    print("_______________________________________________")
    print("The difference of ",num1," and ",num2,"is:")
    difference=int(input())
    if num1-num2 != difference:
        print("you answered Incorrect.")
    else:
        print("you answered Correct.")
    print("_______________________________________________")
    myfun()
myfun()

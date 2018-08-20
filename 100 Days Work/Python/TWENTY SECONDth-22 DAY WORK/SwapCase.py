"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

Sample input  1   -> Www.HackerRank.com → wWW.hACKERrANK.COM
Sample output 1  -> Pythonist 2 → pYTHONIST 2

Sample Input  2   ->HackerRank.com presents "Pythonist 2".
Sample Output 2  ->hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""

str=input("Enter a string::")

for i in str.split( ):
    if(len(i)>1):
        if(i[0].islower() and i[1].lower()):
            print(i[0:len(i)].upper(), end=' ')
        else:
            print(i[0:len(i)].swapcase(),end=' ')
    elif(i[0].lower()):
        print(i[0].upper(),end=' ')
    else:
        print(i[0].lower(),end=' ')








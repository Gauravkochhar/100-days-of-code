"""
Sample Input->  ABCDEFGHIJKLIMNOQRSTUVWXYZ
                4

Sample Output->

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""



import textwrap
if(__name__=='__main__'):
    string=input()
    width=int(input())
    lines=textwrap.wrap(string,width)
    for i in lines:
        print(i)

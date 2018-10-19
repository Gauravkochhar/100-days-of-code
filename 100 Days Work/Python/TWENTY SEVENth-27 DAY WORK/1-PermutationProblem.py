'''
Sample Input
HACK 2

Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
'''


from itertools import permutations
if __name__=='__main__':
    ls,size=input().split()
    for i in list(permutations(sorted(ls),int(size))):
        print(''.join(i),end="\n")

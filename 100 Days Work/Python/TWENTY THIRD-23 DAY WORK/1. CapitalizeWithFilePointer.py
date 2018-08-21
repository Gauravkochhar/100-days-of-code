"""
Sample Input->  chris alan
Sample Output-> Chris Alan

"""
import math
import os
import random
import re
import sys
def solve(s):
    ls=s.split()
    newls=[]
    for i in ls:
        newls.append(i.title())
    r=""
    r=' '.join(i for i in newls)
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()

    """
    ANOTHER WAY
    
    r=""
    r=' '.join(i.capitalize() for i in s.split(' '))
    return r
    
    """

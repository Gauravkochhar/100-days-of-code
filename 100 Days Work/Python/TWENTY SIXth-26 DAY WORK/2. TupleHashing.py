"""
Sample Input->
2
1 2

Sample Output-> 3713081631934410656
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    inputlist=tuple(integer_list)
    s=hash(inputlist)
    print(s)

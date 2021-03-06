"""
The first line contains the number of shoes. 
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains the number of customers. 
The next  lines contain the space separated values of the shoe size desired by the customer and xi, the price of the shoe.


Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output

200
Explanation

Customer 1: Purchased size 6 shoe for $55. 
Customer 2: Purchased size 6 shoe for $45. 
Customer 3: Size 6 no longer available, so no purchase. 
Customer 4: Purchased size 4 shoe for $40. 
Customer 5: Purchased size 18 shoe for $60. 
Customer 6: Size 10 not available, so no purchase.

Total money earned = 55+45+40+60=200

"""


import collections
if __name__=='__main__':
    n_of_s=int(input("Number of shoes:"))
    Shoe_sizes=collections.Counter(map(int,input().split()))
    n_of_c=int(input())
    Sale=0
    for i in range(n_of_c):
        size,price=map(int,input().split())
        if (Shoe_sizes[size]>=1):
            Sale=Sale+price
            Shoe_sizes[size]=Shoe_sizes[size]-1
    print(Sale)

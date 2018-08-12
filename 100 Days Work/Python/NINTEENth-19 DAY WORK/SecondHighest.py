if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    largest1=arr[0]
    for i in range(n):
        if(arr[i]>largest1):
            largest1=arr[i]
    largest2=arr[0]
    for i in range(n):
        if(arr[i]>largest2 and arr[i]<largest1):
            largest2=arr[i]
    print("*************************************")
    print("Second largest value is :",largest2)
    print("*************************************")

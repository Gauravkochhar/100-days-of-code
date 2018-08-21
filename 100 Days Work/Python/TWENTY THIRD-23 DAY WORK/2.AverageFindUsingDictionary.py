"""
Sample Input 

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika


Sample Output->     56.00
"""



if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    student_marks[query_name]
    values=[]
    values=student_marks[query_name]
    avg=0
    sum=sum(values)
    avg=(sum/len(values))
    print("{0:.2f}".format(avg))

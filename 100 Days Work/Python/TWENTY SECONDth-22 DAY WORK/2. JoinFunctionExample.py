"""
Sample Input   ->   this is a string   
Sample Output  ->   this-is-a-string

"""





def split_and_join(line):
    list=[]
    list=line.split()          
    s='-'
    words=s.join(list)
    print(words)
        
line=input()
split_and_join(line)
if __name__=='__main__':

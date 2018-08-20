"""
Sample Input->     abracadabra
                   5 k
                 
                 
Sample Output->    abrackdabra


"""



def mutate_string(string, position, character):
    list1=[]
    list1=list(string)
    list1[int(position)]=character
    s=''.join(list1)    
    return s
if __name__=='__main__':
  s=input("")
  p,c = input("").split(' ')
  s=mutate_string(s,p,c)  
  print(s)

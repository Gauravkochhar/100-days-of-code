"""
Sample Input->  BANANA

logical Output->  ['B',
                  'BA',
                  'BAN',
                  'BANA',
                  'BANAN',
                  'BANANA', 'A',
                            'AN',
                            'ANA',
                            'ANAN',
                            'ANANA',
                                     'N',
                                     'NA',
                                     'NAN',
                                     'NANA',
                                             'A',
                                             'AN',
                                             'ANA', 
                                                   'N',
                                                   'NA',
                                                       'A']
"""


s=input("Enter a String:")
a=[]
k=0
for j in range(k,len(s)):
    for i in range(len(s)+1):
        a.append(s[k:i])
    k=k+1
while a.count(''):
    a.remove('')
print(a)

#from itertools import count
#import numbers
#import keyword
#print(keyword.kwlist)
#print(len(keyword.kwlist))
#for value in keyword.kwlist:
 #   print(value)
#number= 'Indexial'
#while True :
#    print(number,end=' !!!!!  ')
   # number += 1
    
def m1(n) :
    def m2():
        x = n ()
        return x + 2
    return m2    
def m3():
    return 10

result = m1(m3)
r = result() 
print(r) 


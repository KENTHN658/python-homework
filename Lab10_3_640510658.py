
import string

def patterned_message(message, pattern):
    b2 = len(message)
    #print(pattern)
    q1 = message 
    q1 = q1.split(' ')
    r1 = []
    for i in q1: #message
        #print(i)  #message
        for j in i:  #message 
            r1.append(j)  #message
    #print(r1)#['1', '2', '3']
    b1 = len(r1)  #message
    a1 = pattern.split('\n') 
    #print(type(a1))
    p1 = len(pattern)
    #print(a1)
    c1 = []
    c2 = []
    for i in a1:
        x1 = (i.lstrip())
        c1.append(x1)
    #print(c1) #['** *** ** ** *']
    c2 = []
    #print(c1)
    for i in c1:
        #for j in i:
            x2 = (i.split('\n'))
            c2.append(x2)
    #print(c1[0])
    #print(c1[1])
    #print(c1[0])
    k = 0
    for i in pattern:
       
            if i =="*":
                print(r1[k],end="")
                k = k + 1
                k = k % b1
            else:
                print(i,end="")
    
    
    



"""
#patterned_message("123","** *** ** ** *")

#patterned_message("D and C",'''
***************
******   ******
***************
''')

#patterned_message("Three Diamonds!",''' 
    *     *      *
   ***   ***    ***
  ***** *****  *****
   ***   ***    ***
    *     *      *
  ''') """


import string

def decode(code_table, text):
    q1 = code_table #aceiklmr-
    #print(q1)
    a1 = text.split('\n') #['3 ', '                    5 3 4 2 ', '                    3 1 2 8 1 7 2 0 86']
    #print(type(a1))
    p1 = len(code_table)
    #print(a1)
    c1 = []
    c2 = []
    for i in a1:
        x1 = (i.lstrip())
        #x1 = (i.rstrip())
        c1.append(x1)
    #print(c1)
    for i in c1:
        x2 = (i.rstrip())
        c2.append(x2)
    w1 = []
    for i in c2:
        d1 = (i.split(" "))
        w1.append(d1)
    #print(w1) #[['3'], ['5', '3', '4', '2', ''], ['3', '1', '2', '8', '1', '7', '2', '0', '86']]
    for i in w1:
        for k in i:
            k = int(k)
            #print(type(k))
            if k < 0:
                print("_",end="")
            elif k < p1:
                print(q1[k],end="")
            else:
                print("_",end="")
        print()


def main():
    decode("aceiklmr-",'''-3 
                    5 3 4 2 
                    3 1 2 8 1 7 2 0 86''')


if __name__ == '__main__':
    main()
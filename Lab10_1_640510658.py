def square_frame(n, sep=' '):
    a1 = []
    for k in range (n*n):
        a1.append('{:02}'.format(k))
    del a1[0]
    #print(a1)
    op = (n-1)*4
    del a1[op:]
    for i in range(n):
        k = 0
        o = -1
        p = -1
        for j in range(n):
            if i == 0 :
                print("{:}".format(a1[k]),end="")
                k = k+1
                if j<(n-1):
                    print(sep,end="")
            elif (i>0 and i<(n-1)) :
                if j==0 or j==(n-1):
                    print("{:}".format(a1[p]),end="")
                    del a1[p]
                    p = 0
                    #print(a1)
                else:
                    if n == 3 and j==1:
                        print(sep*(4),end="")
                    elif  j==1:
                        print(sep*((n-3)*3+4),end="")
            elif i == (n-1):
                print("{:}".format(a1[o]),end="")
                o = o -1
                if j<(n-1):
                    print(sep,end="")
        del a1[:k] 
        print()
        
  
def main():
    #square_frame(3,'.')
    #print()
    #square_frame(3)
    #square_frame(4,'.')
    #print()
    #square_frame(4)
    #print()
    square_frame(6)
    #print()
    square_frame(7)


if __name__ == '__main__':
    main()

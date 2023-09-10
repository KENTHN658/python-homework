

#ที่มาครับ
def matrix_mult(X,Y): #https://www.programiz.com/python-programming/examples/multiply-matrix
    t = []
    u1 = len(list(X[0])) #3
    #e1 = len(list(X)) #2
    #u2 = len(list(Y[0])) #2
    e2 = len(list(Y)) #3
    if e2 != u1:
        return None
    
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
    for r in result:
        t.append(r)
    return t
        

    
    
    
 

def main():
    x =[[1,2,3],
        [4,5,6]]
    y =[[7,8],
        [9,10],
        [11,12]
        ]
    print(matrix_mult(x,y))
  

if __name__ == "__main__":
    main()
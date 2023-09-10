def square_matrix(list_x):
    p = [] 
    f = len(list_x) 
    p.append(f)
    for i in list_x: #หาตัวมาก
        z = len(i)
        p.append(z)
    #print(p)
    c = max(p) #[2, 4, 3]
    #print(c) # 4
    while len(list_x) < c:
        k = []
        for i in range(c):
            k.append(0)
        list_x.append(k)
    for i in range(c):
        while len(list_x[i]) < c:
            list_x[i].append(0)

    


def main():
    list_x = [[1, 2],
[1, 2, 3],
[1, 2],
[1, 2],
[1]]
    print(square_matrix(list_x))
    print(list_x)
    
    





if __name__=='__main__':
    main()
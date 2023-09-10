def n_base_to_10(n, num,m = 0):
    if type(num) != list:
        x = list(str(num))
    else:
        x = num
    p = len(x) - 1
    v = int(x[0])*((n)**p)
    #print(v)
    del x[0]
    m = m + v
    #print(m)
    if len(x) != 0:
        return n_base_to_10(n,x,m)
    else:
        return m
   


def main():
    n = 4
    num = 231

    print(n_base_to_10(n, num))


if __name__=='__main__':
    main()
def subset(set_a, n):
    import math
    set_b = sorted(list(set_a))
    #if n == 0:
        #return [set()]
    list_set = []
    if n >= 0:
        op = len(set_b)
        for i in range (1 << op): 
            pol = []
            for j in range(op):
                if (i & (1 << j)):
                    pol.append(set_b[j])
            #print(pol)
            list_set.append(pol)
    zp = []
    for i in list_set:
        fg = (len(set(i)))
        if fg <= n:
            zp.append(set(i)) 
            continue
    #print(list_set)
    return (zp)
    




def main():
    set_a = {'a', 'b', 'c'}
    b = 9
    print(subset(set_a, b))




if __name__=='__main__':
    main()
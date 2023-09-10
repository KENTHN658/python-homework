def gcd(x, y):
    import math
    if max(x,y) / min(x,y) == max(x,y) // min(x,y):
        return min(x,y)
    b = max(x,y) / min(x,y)
    c = min(x,y)
    m =(b - int(b))*c
    m =round(m)
    if c % m == 0:
        return m
    elif c % m > 1:
        return gcd(c,m)
    elif c % m == 1:
        return 1





def main():
    print(gcd(19, 71))
    print(gcd(1071, 462))
    print(gcd(79, 38))
    print(gcd(78, 39))




if __name__=='__main__':
    main()
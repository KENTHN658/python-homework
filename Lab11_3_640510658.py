import math
def prime_factor(n):
    i = 2
    num = []
    while i <= math.sqrt(n):
        if n % i == 0:
            n = n / i
            num.append(i)
            
            continue
        else:
            i = i+1  
    num.append(int(n))
    return num


def coprime_factor(a, b):
    yu = abs(a)
    ru = abs(b)
    i = 2
    deng = []
    lunlun = {}
    dengdeng = {}
    lun = prime_factor(yu)
    #print(lun)
    deng = prime_factor(ru)
    #print(deng)
    for i in lun:
        if i in lunlun:
            lunlun[i] = lunlun[i] + 1
        else:
            lunlun[i] = 1
    #print(lunlun)
    for i in deng:
        if i in dengdeng:
            dengdeng[i] = dengdeng[i] + 1
        else:
            dengdeng[i] = 1
    #print(dengdeng)
    dk = []
    lun2 = set()
    for i in lun:
        lun2.add(i)
    for i in lun2:
        #print(i)
        if i in lunlun and  i in dengdeng:
            if lunlun[i] <= dengdeng[i]:
                for k in range(lunlun[i]):
                    dk.append(i)
            elif lunlun[i] > dengdeng[i]:
                for l in  range(dengdeng[i]):
                    dk.append(i)
    dk.sort()
    return  dk
        
            
def main():
    a = 164115
    b = 1406700
    print(coprime_factor(a, b))


if __name__=='__main__':
    main()
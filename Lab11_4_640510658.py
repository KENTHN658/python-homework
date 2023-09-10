def polynomial_addition(p1, p2):
    from operator import itemgetter
    #print(p1)
    #print(p2)
    x1 = sorted(p1, key=itemgetter(0),reverse = True)
    
    #print(x1)
    x2 = sorted(p2, key=itemgetter(0),reverse = True)
    #print(x2)
    list1 = [] #[2, 1, 0]
    list2 = [] #[2, 1, 0]
    sate1 = set()
    sate2 = set()
    for i in x1:
        list1.append(i[0])
        sate1.add(i[0])
    #print(list1)
    for i in x2:
        list2.append(i[0])
        sate2.add(i[0])
    #print(list2)

    w1 = (sate1 & sate2)
    w2 = sate1 | sate2
    w3 = list(w2 - w1) #[3, 4]

    #print(w2)
    #print(w3)
    w1 = list(w1)
    #print(w1)
    d1 = {}
    d2 = {}
    for i in x1:
        d1[i[0]] = i[1]
    #print(d1)
    for i in x2:
        d2[i[0]] = i[1]
    #print(d2)
    d3 = {}
    for i in w1:
        cv = d1[i] + d2[i]
        d3[i]=cv
    #print(d3) #{2: 0, 1: 35, 0: -6}
    dave = []
    jave = []
    for i in d3:
        #print(i)
        if d3[i] != 0:
            dave.append(d3[i])
            jave.append(i)
            #print(d3[i])
            #print(i)
    #print(dave)
    #print(jave)
    de = []
    ja = []
    for i in w3:
        if i in d1:
            com = d1[i]
            de.append(com)
            ja.append(i)
        elif i in d2:
            com = d2[i]
            de.append(com)
            ja.append(i)
    vu = zip(ja,de) 
    pb = (list(vu))     
    exam = list(zip(jave,dave))
    exam.extend(pb) #[(0, -6), (1, 35), (9, 3), (1, 4)]
    
    habor = sorted((exam),key=itemgetter(0),reverse=True)
    #print(habor) #[(1, 35), (0, -6)]'''
    return habor

    





def main():
    p1 = [(2, 6), (1, 34), (0, -8),(3, 9)]
    p2 = [(2, -6), (0, 8), (1, 1),(4, 1)]
    print(polynomial_addition(p1, p2))
    #print(p1)
    #print(p2)


if __name__=='__main__':
    main()

def three_letters_count(text):
    text = text.lower()
    text = text.split('\n')
    #print(text)
    x = text
    #print(x)
    hhh = []
    for i in x:
        pk = (i.split(' '))
        hhh.extend(pk)
    #print(hhh)
    kkk = []
    for i in hhh:
        if i == '':
            del i
        else:
            kkk.append(i)
    #print(kkk)

    
    yg = len(x)
    #print(yg)
    gg = []
    for i in kkk:
        #print(i)
        c = 0
        b = 3
        while b <= len(i):
            gg.append(i[c:b])
            c = c + 1
            b = b + 1
        if len(i) < 3:
            gg.append(i)
    dkf = {}
    for k in gg:
        if k in dkf:
            dkf[k] = dkf[k] +1
        else:
            dkf[k] = 1
    return (dkf)

    

    
    


def main():
    x = '''Wish you all 
    good luck for the exam
    in a aaa aa a''' 

    print(three_letters_count(x))


if __name__ == '__main__':
    main()
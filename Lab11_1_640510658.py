def  sort_date(list_x):
    a = []
    d_m_y = []
    year = []
    month = []
    day = []
    dyear = {}
    dmonth = {}
    dday  = {}
    dfog = {}
    for i in list_x:
        x = i.split("/")
        #print(x)
        year.append(x[2])
        month.append(x[1])
        day.append(x[0])
        d_m_y.append(x[:])
        dyear[x[2]]=i
        dmonth[x[1],x[2]]=i
        dday[x[0],x[1],x[2]]=i
    del list_x[:]
    #print(year) #['2100', '1999', '2003', '2001']
    xyearnormal = len(year)
    xyearset = len(set(year))
    #print(xyearnormal)
    #print(xyearset)
    #print(month) #['1', '12', '1', '9']
    xmonthnormal = len(month)
    xmonthset = len(set(month))
    #print(xmonthnormal)
    #print(xmonthset)
    #print(day) #['11', '5', '19', '11']
    #print(dyear) #{'2100': '11/1/2100', '1999': '5/12/1999', '2003': '19/1/2003', '2001': '11/9/2001'}
    #print(dmonth) #{('1', '2100'): '11/1/2100', ('12', '1999'): '5/12/1999', ('1', '2003'): '19/1/2003', ('9', '2001'): '11/9/2001'}
    #print(dday) #{('11', '1', '2100'): '11/1/2100', ('5', '12', '1999'): '5/12/1999', ('19', '1', '2003'): '19/1/2003', ('11', '9', '2001'): '11/9/2001'}
    if xyearnormal == xyearset:
        cv = sorted(year)
        #print(cv)
        for i in cv:
            dm = (dyear[i])
            list_x.append(dm)
        #return list_x
    else:
        n1 = len(year)
        for i in range(n1):
            b1 = (int(year[i])*365) + (int(month[i])+30) + (int(day[i]))
            dfog[b1] = d_m_y[i]
            a.append(b1)
        #print(dfog)
        aa = sorted(a)
        #print(aa)
        qq = []
        for i in aa:
            dm = dfog[i]
            dm = tuple(dm)
            qq.append(dm)
        #print(qq)
        for i in qq:
            dm = (dday[i])
            list_x.append(dm)
        #return list_x
        


    #return list_x


def main():
    list_x = ["11/1/210", "11/1/2100", "11/1/2100", "18/9/200000"]
    sort_date(list_x)
    print("---")
    print(list_x)

   
    list_x = ["11/1/2100", "5/12/1999", "19/1/2003", "11/9/2001"]
    sort_date(list_x)
    print("---")
    print(list_x)


if __name__ == '__main__':
    main()
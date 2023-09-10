def  search_event(list_x, key):
    deng = key.split('/')
    #print(deng)
    key1 = []
    for i in deng:
        lun  = int(i)
        lun  = str(lun)
        key1.append(lun)
    #print(key1)
    devent = {}
    for i in list_x:
        la = i[0]
        ba = la.split('/')
        noon = tuple(ba)
        #print(noon)
        #print(ba)
        #print(la)
        devent[noon] = i
        #print(i)
    #print(devent) #{('11', '1', '1900'): ('11/1/1900', 'Event A'), ('5', '12', '2001'): ('5/12/2001', 'Event B'), ('5', '12', '2002'): ('5/12/2002', 'Event C'), ('21', '8', '2008'): ('21/8/2008', 'Event D'), ('9', '3', '2013'): ('9/3/2013', 'Event E'), 
                  #('11', '3', '2017'): ('11/3/2017', 'Event F'), ('7', '5', '2019'): ('7/5/2019', 'Event G'), ('29', '2', '2032'): ('29/2/2032', 'Event H'), ('9', '11', '2042'): ('9/11/2042', 'Event I')}
    key2 = tuple(key1)
    #print(key2)
    if key2 in devent:
        return (devent[key2])
    else:
        return None




def main():
    list_x = [("11/1/1900", "Event A"), ("5/12/2001", "Event B"),
                ("5/12/2002", "Event C"), ("21/8/2008", "Event D"),
                ("9/3/2013", "Event E"), ("11/3/2017", "Event F"),
                ("7/5/2019", "Event G"), ("29/2/2032", "Event H"),
                ("9/11/2042", "Event I")]
    event = search_event(list_x, "29/02/2032")
    print("---")
    print(event)





if __name__ == '__main__':
    main()
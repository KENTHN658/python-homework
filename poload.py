def is_in_q1(circle):
    #print(circle)
    x = (circle[0])
    y = (circle[1])
    r = (circle[2])
    if x > 0 and y > 0:
        return True
    if y + r > 0 and x > 0:
        return True
    if x + r > 0 and y > 0:
        return True
    else:
        return False
def is_in_q2(circle):
    x = (circle[0])
    y = (circle[1])
    r = (circle[2])
    if x < 0 and y > 0:
        return True
    if y + r > 0 and x < 0:
        return True
    if x - r < 0 and y > 0:
        return True
    else:
        return False

def is_in_q3(circle):
    x = (circle[0])
    y = (circle[1])
    r = (circle[2])
    if x < 0 and y < 0:
        return True
    if (x - r < -0) and y < 0:
        return True
    else:
        return False
def is_in_q4(circle):
    x = (circle[0])
    y = (circle[1])
    r = (circle[2])
    if x > 0 and y < 0:
        return True
    if y - r < 0 and x > 0:
        return True
    if x + r > 0 and y < 0:
        return True
    else:
        return False


def count_segment(list_a):
    #print(list_a)
    a0 = []
    a1 = 0
    a2 = 0 
    a3 = 0
    a4 = 0
    for i in list_a:
        if is_in_q1(i) == True:
            a1 = a1 + 1
    a0.append(a1)
    for i in list_a:
        if is_in_q2(i) == True:
            a2 = a2 + 1
    a0.append(a2)
    for i in list_a:
        if is_in_q3(i) == True:
            a3 = a3 + 1
    a0.append(a3)
    for i in list_a:
        if is_in_q4(i) == True:
            a4 = a4 + 1
    a0.append(a4)
    return tuple(a0)

def top_bottom_left_right(list_a):
    t = 0
    b = 0
    l = 0 
    r = 0 
    b0 = []
    for i in list_a:
        if (is_in_q1(i) == True) or (is_in_q2(i) == True):
            t = t + 1
    b0.append(t)
    for i in list_a:
        if (is_in_q3(i) == True) or (is_in_q4(i) == True):
            b = b + 1
    b0.append(b)
    for i in list_a:
        if (is_in_q2(i) == True) or (is_in_q3(i) == True):
            l = l + 1
    b0.append(l)  
    for i in list_a:
        if (is_in_q1(i) == True) or (is_in_q4(i) == True):
            r = r + 1
    b0.append(r)
    p = []
    for i in b0:
        if b0 == 0:
            p.append(" ")
        else:
            p.append(i)

    return tuple(p)
       
    




def main():
    """
    print(is_in_q1((2, 7, 1.5)))
    print(is_in_q1((3.2, 2.5, 4.06)))
    print(is_in_q1(((-5.5, -4.5, 2.5))))
    print(is_in_q1(((2, -5.2, 3))))
    print(is_in_q1((7.2, -2.8, 1.2)))
    print()
    print(is_in_q2((2, 7, 1.5)))
    print(is_in_q2((3.2, 2.5, 4.06)))
    print(is_in_q2(((-5.5, -4.5, 2.5))))
    print(is_in_q2(((2, -5.2, 3))))
    print(is_in_q2((7.2, -2.8, 1.2)))
    print()
    print(is_in_q3((2, 7, 1.5)))
    print(is_in_q3((3.2, 2.5, 4.06)))
    print(is_in_q3(((-5.5, -4.5, 2.5))))
    print(is_in_q3(((2, -5.2, 3))))
    print(is_in_q3((7.2, -2.8, 1.2)))
    print()
    print(is_in_q4((2, 7, 1.5)))
    print(is_in_q4((3.2, 2.5, 4.06)))
    print(is_in_q4(((-5.5, -4.5, 2.5))))
    print(is_in_q4(((2, -5.2, 3))))
    print(is_in_q4((7.2, -2.8, 1.2)))
    print()'''"""
    #list_a = [(2, 7, 1.5), # a
    #(3.2, 2.5, 4.06), # b
    #(-5.5, -4.5, 2.5), # c
    #(2, -5.2, 3), # d
    #(7.2, -2.8, 1.2)] 
    #rint(count_segment(list_a))
    list_a = [(2, 7, 1.5), # a
    (3.2, 2.5, 4.06), # b
    (-5.5, -4.5, 2.5), # c
    (2, -5.2, 3), # d
    (7.2, -2.8, 1.2)]
    print(top_bottom_left_right(list_a))




if __name__ == '__main__':
    main()
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





def main():
    print(is_in_q1((2, 1, 3)))
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
    print(is_in_q4((2, 5, 1.5)))
    print(is_in_q4((3.2, 2.5, 4.06)))
    print(is_in_q4(((-5.5, -4.5, 2.5))))
    print(is_in_q4(((2, -5.2, 3))))
    print(is_in_q4((7.2, -2.8, 1.2)))



if __name__ == '__main__':
    main()
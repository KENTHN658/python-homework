def reverse_num(num,y=0,z=''):
    if type(num) != list:
        num = list(str(num))
    #print(num)
    y = len(num)
    y = y - 1
    #print(y)
    if y >= 0:
        z = z + num[y] 
        del num[y]
        return reverse_num(num,y,z)
    if y<0:
        return int(z)
def main():
    print(reverse_num(4321))
    print(reverse_num(3412))
    print(reverse_num(1331))


if __name__=='__main__':
    main()
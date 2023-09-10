def is_palindrome(x, b):
    decimal = x
    base = b
    binary = []
    binary02 = []
    while decimal > 0:
        a1 = decimal % base
        binary.append(a1)
        binary02.append(a1)
        #binary.append(decimal % base)
        #binary02.append(decimal % base)
        decimal = (decimal // base)
    #print(binary)
    binary.reverse()

    x1 = binary02
    #print(x1)
    x2 = binary
    #print(x2)
    if x1 == x2:
        return True
    else:
        return False

def main():
    print(is_palindrome(358865,8))


if __name__ == '__main__':
    main()
 

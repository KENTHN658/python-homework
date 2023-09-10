def love6(first, second):
    # WRITE YOUR CODE HERE
    if first == 6:
        return True
    if second == 6:
        return True
    elif first + second == 6:
        return True
    elif abs(first - second) == 6:
        return True
    else:
        return False
     

def main():
    # receive input from user
    first = int(input())
    second = int(input())
    # print result from function3
    print(love6(first,second))

if __name__ == '__main__':
    main()

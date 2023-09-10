def sum_nested_list(x):
    a1 = 0
    while len(list(x)) != 0:
        if isinstance(x[0],int):
            a1 = a1 + x[0]
            
            del x[0]
        elif isinstance(x[0],list):
            x.extend (x[0])
            del x[0]
    return a1


def main():
    x =[81, [[31, [159]], 9577, [22, [181, [41]]]]]
    print(sum_nested_list(x))
    

if __name__ == '__main__':
    main()
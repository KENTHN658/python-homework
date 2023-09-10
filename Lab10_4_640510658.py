import string


def uniform(line):
    small = 0
    big = 0
    for word in line:
        if word in string.ascii_lowercase:
            small = small + 1
        if word in string.ascii_uppercase:
            big = big + 1
    if big>small:
        x = line.upper()
        return x
    elif small > big:
        x = line.lower()
        return x
    else:
        if line[0] in  string.ascii_lowercase:
            x = line.lower()
            return x
        else: 
            x = line.upper()
            return x
            
        
def main():
    line = 'HaPpY'
    print(uniform(line))
    print()

    line = 'cOdINg'
    print(uniform(line))
    print()
    
    line = 'coMP scI!!!'
    print(uniform(line))
    print()



if __name__ == '__main__':
    main()
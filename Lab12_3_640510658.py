def is_prime(n, k =2):
    if n % k != 0 and k < n:
        k = k + 1
        return is_prime(n, k)
    if n % k == 0 and k < n:
        return False
    else:
        return True
    
    

def main():
    n = 21
    print(is_prime(n))




if __name__ == '__main__':
    main()
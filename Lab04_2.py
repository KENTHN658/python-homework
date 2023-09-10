#!/usr/bin/env python3
# ชื่อ นามสกุล
# รหัสนักศึกษา
# Lab 04
# Problem 2
# 204111 Sec ???

def my_max_mid_min(a, b, c):
    # WRITE YOUR CODE HERE
    if a > b:
    	max = a
    	min = b
    else:
    	max = b
    	min = a
    
    if c >= max:#ย้ายค่าตัวแปลไปมา
        mid = max
        max = c
    elif c <= min:
    	mid = min
    	min = c
    elif min <= c <= max:
        mid = c

    
    print("max = ",max)
    print("mid = ",mid)
    print("min = ",min)

def main():
    # receive input from user
    a = int(input())
    b = int(input())
    c = int(input())
    # call function
    my_max_mid_min(a, b, c)

if __name__ == '__main__':
    main()

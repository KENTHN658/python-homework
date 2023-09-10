#!/usr/bin/env python3
# ธนธรณ์ บุญเชิด
# 640510658
# Lab 04
# Problem 5
# 204111 Sec 002

def nearest_odd(x):
    # WRITE YOUR CODE HERE
    if x==0:
    	return 0
    if int(x)%2 == 0:
    	b = int(x)+1
    	return b
    if x%2 != 0:
    	return int(x)
    if x < 0 and x%2 == 0:
    	x2 = abs(x)
    	m = math.ceil(x2)
    	m2 = x + m
    	m3 = abs(m2)
    	x3 = x + m3 +1
    	return x3
    	
    	
    else:
    	return int(x)
    	

def main():
    # receive input from user
    x = float(input())
    # print result from function
    print(nearest_odd(x))

if __name__ == '__main__':
    main()

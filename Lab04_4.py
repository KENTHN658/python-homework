#!/usr/bin/env python3
# ชื่อ นามสกุล
# รหัสนักศึกษา
# Lab 04
# Problem 4
# 204111 Sec ???
import math
def round_to_int(x):
    # WRITE YOUR CODE HERE
    c = math.floor(x)
    c2 = x-c
    if x >= 0:
    	c = math.floor(x)
    	c2 = x - c
    if c2 >= 0.5:
    	c3 = math.ceil(x)
    	return c3
    if c2 < 0.5:
    	return c
    if x < 0:
    	b = math.floor(x)
    	b2 = x - b
    if b2 <= 0.5:
    	return b
    if b2 > 0.4:
    	d = x
    	a = math.ceil(x)
 
    
    	
 
    	

def main():
    # receive input from user
    x = float(input())
    # print result from function
    print(float(round_to_int(x)))

if __name__ == '__main__':
    main()

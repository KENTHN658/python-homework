#!/usr/bin/env python3
# ธนธรณ์ บุญเชิด
# 640510658
# Lab 04
# Problem 3
# 204111 Sec 002

def calculate_p2p_evolve_exp(p, c):
    # WRITE YOUR CODE HERE
    
    if c and p ==0:
    	return 0
    if (p>c) and (p<= 10):
    	exp0 = (((p-1)+c)) // 12  *500
    	return exp0
    if  (p<c) :
    	exp0 = (((p-1)+c) // 12) *500
    	return exp0
   
    candy1 = c // 12
    if candy1 == p:
    	exp1 = p*500
    elif candy1 > p:
    	exp1 = p*500
    elif candy1 < p:
    	exp1 = candy1*500
    candy2 = exp1//500
    candy3 = c - ((exp1//500) * 12)
    candy4 = candy2 + candy3
   
    p2 = p - exp1//500
    p3 = p2 -1
    candy5 = p3 + candy4
    if p2 > 12:
    	exp2 = (candy5  //12)*500
    	return exp1 + exp2
    else:
    	return exp1
    
def main():
    # receive input from user
    p = int(input())
    c = int(input())
    # print result from function
    print(calculate_p2p_evolve_exp(p, c))

if __name__ == '__main__':
    main()

#!#!/usr/bin/env python3
# ธนธรณ์ บุญเชิด
# 640510658
# Lab 07
# Problem 1
# 204111 Sec 002
import math
def main():
    x  = int(input())
    y  = int(input())
    #prime_in_range(x, y)
    if x != y:
      print(sum_prime_in_range(x, y))
    elif x == y:
      print(y)
def sum_prime_in_range(x, y):
  cake = 0
  for i in range (x, y+1):
    #print(i)
    flag = 0

    for j in range(2, i):
      
      if (i % j == 0):
        flag = 1
        break
      
    if (flag == 0):
      #print(i)
      #print(type(i))
      cake = cake + i
  return cake
  
  
    
    

if __name__ == '__main__':
    main()

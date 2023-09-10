#!/usr/bin/env python3
# ชื่อ นามสกุล
# รหัสนักศึกษา
# Lab 06
# Problem 3
# 204111 Sec ???

import math
def factorize(num):
  x = num
  print("%d" %num + " is ",end="")
  i = 2 
  while i <= math.sqrt(num):
    if num % i == 0:
      #print("a")
      num = num / i
      print(i,end=" "+"*"+" ")
      #print(num)
      continue
    else:
      i = i+1
  #print("num = ",num)
  #print("x =", x)
  if num > 2  and num==x:
    #print("a")
    print("prime")
  elif num >= 2:
    #print("aaaaaa")
    print(int(num))
  k = "1 is 1"  
  if x == 1:
    #print("b")
    print (k)
  kk ="0 is 0"
  if x == 0:
    #print("c")
    print (kk)
  
  
    
  

def main():
    num = int(input("input_num: "))
    factorize(num)
    

if __name__ == '__main_q_':
    main()

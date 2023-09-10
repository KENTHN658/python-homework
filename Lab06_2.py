#!/usr/bin/env python3
# ธนธรณ์ บุญเชิด
# 640510658
# Lab 06
# Problem 2
# 204111 Sec 002


def float_to_bin(x):
  k = 0
  b = 0
  x1 = x
  x = abs(x)
  jj = x
  x = int(x)
  while x != 0:
    a = x %  2
    b = b + (a * (10**k))
    x = x // 2
    k = k+1
  
  p = -1
  jj = jj % 1 #เอาทศนิยมอย่างเเดียว
  re = 0
  for i in range(6):
    jj = jj * 2
    re  = re + (int(jj)*10**p)
    jj = jj - int(jj)
    p = p - 1
  

  
  if x1 >= 0:
    return (b + re)
  elif x1 < 0 :
    return -(b+re)
  
    
def main():
    x = float(input())
    print(float_to_bin(x))
    

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
# ธนธรณ์ บุญเชิด
# 640510658
# Lab 06
# Problem 1
# 204111 Sec 002


def int_power(x, y):
  al = 1
  
  if y >= 0:
    for i in range(y):
      al = al*x
    return al
  elif y<0:
    al = x**y
    return al
  
    
    
  

def main():
    x = float(input())
    y = int(input())
    print("{:.6f}".format(int_power(x,y)))
    
    
if __name__ == '__main__':
    main()


#!/usr/bin/env python3
# ธนธรณ์
# 640510658
# Lab 03
# Problem 2
# 204111 Sec 002

def reverse_digits(x):
   c = (x % 10) * 1000
   v = ((x // 10) % 10) * 100
   b = (x // 100) % 10 * 10
   n = x // 1000
   a = c+v+b+n
   return a
  
  

def main():
    # รับตัวเลขจาก user
    x = int(input())
    # พิมพ์ตัวเลขกลับด้าน
    print(reverse_digits(x))

if __name__ == '__main__':
    main()

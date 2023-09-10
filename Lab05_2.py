#!/usr/bin/env python3
# ธนธรณ์ บุญเชิด
# 640510658
# Lab 05
# Problem 2
# 204111 Sec 002

def is_p_triple(x, y, z):
   
   
   if (x**2 + y**2)**0.5 == z: #ใช้สูตรหาสามเหลี่ยม
    return True
   elif (x**2 + z**2)**0.5 == y:
    return True
   elif (z**2 +  y**2)**0.5 == x:
    return True
   else:
    return False

def main():
    x = int(input())
    y = int(input())
    z = int(input())
    print(is_p_triple(x, y, z))

if __name__ == '__main__':
    main()

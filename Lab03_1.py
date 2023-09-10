#!/usr/bin/env python3
# ชื่อ นามสกุล
# รหัสนักศึกษา
# Lab 03
# Problem 1
# 204111 Sec ???

def main():
   # รับข้อมูลพื้นที่ผิวจาก user
   surface_area = float(input("input surface area: "))
   # นำพื้นที่ผิวที่ได้มาคำนวณหารัศมี
   radius = find_r_from_surface_area(surface_area)
   # นำรัศมีที่คำนวณได้มาคำนวณหาปริมาตร
   volume = sphere_volume(radius)
   # แสดงปริมาตรทรงกลม
   print("volume = {0:.2f}".format(volume))

import math


def find_r_from_surface_area(surface_area):
    # เขียนโค้ดเพิ่มตรงนี้
    return (surface_area/(4*math.pi))**0.5

def sphere_volume(radius):
    # เขียนโค้ดเพิ่มตรงนี้
    return (math.pi*4/3*(radius**3))


if __name__ == '__main__':
    main()

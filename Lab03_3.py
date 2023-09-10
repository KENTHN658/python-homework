#!/usr/bin/env python3
# ธนธรณ์  บุญเชิด
# 640510658
# Lab 03
# Problem 3
# 204111 Sec 02

def octagon_area(x):
    # เขียนโค้ดเพิ่มตรงนี้นะจ๊ะ
    area_octagon =(( x / 3 ) * x) + ((x + x/3) * x / 3)
    return area_octagon


def main():
    # รับด้านจาก user
    x = int(input())
    # พิมพ์พื้นที่ของรูปแปดเหลี่ยมด้านเท่า
    print(octagon_area(x))

if __name__ == '__main__':
    main()

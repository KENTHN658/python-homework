#!/usr/bin/env python3
# ธนธรณ์ บุญเซิด
# 640510658
# Lab 03
# Problem 5
# 204111 Sec 002

def main():
    # รับตัวเลขจาก user
    number = int(input('Input number: ')) 
    k = int(input('Input digit: '))
    value = int(input('Input digit: '))
    # พิมพ์ตัวเลขหลังจากการเปลี่ยนค่าหลักที่กำหนด
    print(set_kth_digit(number, k, value))

def kth_digit(number, k):
    # Copy มาจากข้อ 4 ได้เลย
    kth = int(number//10**k)%10
    return kth
    

def set_kth_digit(number, k, value): 
    # เขียนโค้ดเพิ่มเอง ใช้ฟังก์ชัน kth_digit ช่วยได้นะ
    return number + (value-kth_digit(number, k))*10**k

if __name__ == '__main__':
    main()

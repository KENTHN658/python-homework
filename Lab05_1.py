#!/usr/bin/env python3
# ธนธรณ์ บุญเชิด
# 640510658
# Lab 05
# Problem 1
# 204111 Sec 002

#ลอกอาจารย์มาจากในคาบ
#ขอบคุณครับ
def intersects(x1, y1, r1, x2, y2, r2, epsilon=10 ** -6):
    d = ((x1-x2)**2+(y1-y2)**2)**0.5
    if d < abs(r1-r2)-epsilon :
    	return -1
    elif d > r1+r2+epsilon:
        return -1
    elif abs(r1-r2)+epsilon < d and d < (r1+r2)-epsilon:
        return 1
    else:
        return 0
  
def main():
    # receive input from user
    x1 = float(input())
    y1 = float(input())
    r1 = float(input())
    x2 = float(input())
    y2 = float(input())
    r2 = float(input())
    # print result from function
    print(intersects(x1, y1, r1, x2, y2, r2, epsilon=10 ** -6))

if __name__ == '__main__':
    main()

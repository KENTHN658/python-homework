#!/usr/bin/env python3
# ธนธรณ์ บุญเชิด
# 640510658
# Lab 06
# Problem 5
# 204111 Sec 002
#ขอบพระความรุ้จากgoogle
def longest_digit_run(n):
    n = str(n)
    sett = set()
    size = 1
    for ind, elm in enumerate(n):
        if ind > 0:
            if elm == n[ind - 1]:
                size += 1
            else:
                sett.update([size])
                size = 1
    sett.update([size])
    return max(sett)

    
def main():
    n = int(input())
    print(longest_digit_run(n))

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# ชื่อ นามสกุล
# รหัสนักศึกษา
# Lab 06
# Problem 1
# 204111 Sec ???
import math 
def digit_count(x, base=10):
  x1 = abs(x)
  th = math.log(x1, base)
  th2 = math.ceil(th)
  if math.ceil(th) - th <= 10**-6:
    return math .ceil(th)+1
  else:
    return th2


def main():
    x = int(input("number: "))
    base = int(input("base: "))
    #digit_count(x, base)
    if base ==10:
        print(digit_count(x))
    else:
        print(digit_count(x,base))

if __name__ == '__main__':
    main()





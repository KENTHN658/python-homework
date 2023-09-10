#!/usr/bin/env python3
#!/usr/bin/env python3
# ธนธรณ์ บูญเชิด
# รหัสนักศึกษา 640510658
# Lab 08
# Problem 1
# 204111 Sec 002


import string

"""def special(x1):
  special = string.ascii_uppercase #ascii_upp
  special = list(special)          #ตัวอิ้ง  พิมใหญ่
  z1 = []
  for i in special:
    if i in x1:
      z1.append(i)
  return z1

def special02(x2):
  special = string.ascii_uppercase
  special = list(special)
  z2 = []
  for i in special:
    if i in x2:
      z2.append(i)
  return z2"""


def is_anagram(x1, x2):
  special = string.ascii_lowercase
  b1 = x1.lower()
  b2 = x2.lower()
  z1 = []
  z2 = []
  for i in b1:
    if i in special:
      z1.append(i)
  for i in b2:
    if i in special:
      z2.append(i)
  z1.sort()
  z2.sort()
  if z1 == z2:
    return True
  else:
    return False

def main():
  x1 = input()
  x2 = input()
  is_anagram(x1, x2)
 





    


if __name__ == '__main__':
    main()

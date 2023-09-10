#!/usr/bin/env python3
# ธนธรณ์ บุญเชิด
# 640510658
# Lab 05
# Problem 3
# 204111 Sec 


def cal_month(d, m, y):
  if d == 13 and m == 4:
  	month = 13
  	return month
  if (y % 4 == 0) and (m<=4)and(d<=13):
    if m == 1:
      month = 104
    elif m == 2:
      month = 73
    elif m == 3:
      month = 44
      if d<=13:
        if m == 4:
          month = 13
    return month
  x=y%100
  if ((y+1) % 4 == 0) and (m>=4) and (((y+1)%400 <100) or (x%4==0)):
      if m==4:
      	month = 379
      elif m == 5:
      	month = 349
      elif m == 6:
      	month = 318
      elif m == 7:
      	month = 288
      elif m == 8:
      	month = 257
      elif m == 9:
      	month = 226
      elif m == 10:
      	month = 196
      elif m == 11:
      	month = 165
      elif m == 12:
      	month =135
      return month
  if m==1:
    month = 103
  elif m==2:
      month = 72
  elif m==3:
      month = 44
  elif m<=4 and d<=13:
      month = 13
  elif m == 4:
      month = 378
  elif m == 5:
      month = 348
  elif m == 6:
      month = 317
  elif m == 7:
      month = 287
  elif m == 8:
      month = 256
  elif m == 9:
      month =225
  elif m == 10:
      month = 195
  elif m == 11:
      month = 164
  elif m == 12:
      month = 134
  return month
 
    
  

def count_down_to_songkran(d, m, y):
  if d== m== y==0:
  	return "None"
  day = cal_month(d, m, y)
  wansongkran = day - d
  return wansongkran
  
def main():
  d = int(input())
  
  m = int(input())
  
  y = int(input())
  print(count_down_to_songkran(d, m, y))
  


if __name__ == '__main__':
  main()

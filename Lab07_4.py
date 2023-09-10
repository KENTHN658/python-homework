#!/usr/bin/env python3
# ชื่อ นามสกุล
# รหัสนักศึกษา
# Lab 06
# Problem 1
# 204111 Sec ???


def main():
	n = int(input())
	print(life_path(n))
	#print(life_path(n))
	#print(caketh(cake1))

#def caketh(cake1):
  #if cake1 < 10:
    
    
def life_path(n):
	cake = 0
	while n != 0:
	  n2 = n
	  n = n%10
	  cake = cake + n
	  #print(cake,"CAKE")
	  n = n2 // 10
	  #print(n,"NN")
	if n == 0 and cake>10:
	 cake1 = cake
	 return caketh(cake1)
	if (cake<10) and (n==0):
	 return cake


def caketh(cake1):
  cake2 = 0
  while cake1 != 0:
    cake3 = cake1
    cake1 = cake1 % 10
    cake2 = cake2 + cake1
    #print(cake2,"CAKLLL")
    cake1 = cake3 // 10
    #print(cake1,"KOPPP")
  if cake1 == 0 and cake2 == 10:
      #print(1)
    return 1
  if cake1 ==0 and cake2>10:
    return life_path(cake2)
  if cake2<10 and cake1==0:
    return cake2
      
    #return cake2



if __name__ == '__main__':
	main()

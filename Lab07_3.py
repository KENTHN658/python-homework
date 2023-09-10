#!/usr/bin/env python3
# ธนธรณ์ บุญเชิด
# รหัสนักศึกษา
# Lab 06
# Problem 1
# 204111 Sec 002


def main():
	n = int(input())
	triangle(n)

#เขียนไปเรื่อยเด๋วถูกเอง
def triangle(n):
	for i in range(n):
		#print(i)
		for j in range(i + 1):
			#print(i)
			#print("*",end=" ")
			#if i == 1: print("A")
			#print("[",i,",",j,"]",end=" ")
			if j==0 and i==0:
			  print("*",end="  ")
			if j == 0 and i!= n-1 and i != 0:
				print("*", end=".")
			#if  (i+1) == j:
			#print("a",end=" ")
		for j in range(i):
			#print(i)
			#print("[",k,",",i,"]")
			if i - 1 == j and i != n-1:
				print("*", end=" ")
			if i-1 > j and i != n-1:
				print(".", end=".")
		for j in range (i+1):
			if i == n-1:
			  print("*",end=" ")
			#if i-1 > j:
			  #print("*",end =" ")
			   
		

		print()


if __name__ == '__main__':
	main()

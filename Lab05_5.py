#!/usr/bin/env python3
# ธนธรณ์ บุญเชิด
# 640510658
# Lab 05
# Problem 5
# 204111 Sec 002

def zodiac_element(year):
    if year % 12 == 0:
    	b= 'Monkey'
    elif year % 12 == 1:
    	b= "Rooster"
    elif year % 12 == 2:
    	b=  "Dog"
    elif year % 12 == 3:
    	b= "Pig"   
    elif year % 12 == 4:
    	b= 'Rat'
    elif year % 12 == 5:
    	b= "Ox"
    elif year % 12 == 6:
    	b= "Tiger"
    elif year % 12 == 7:
    	b= "Rabbit"
    elif year % 12 == 8:
    	b= 'Dragon'
    elif year % 12 == 9:
    	b="Snake"
    elif year % 12 == 10:
    	b= "Horse"
    elif year % 12 == 11:
    	b= "Goat"
    if (year % 10 == 0) or (year % 10 == 1):
    		a= "Metal"
    elif (year % 10 == 2) or( year % 10 == 3):
    		a= "Water"
    elif (year % 10 == 4) or (year % 10 == 5):
    		a= "Wood"
    elif (year % 10 == 6) or (year % 10 == 7):
    		a= "Fire"
    elif (year % 10 == 8) or (year % 10 == 9):
    		a= "Earth"
    return str(a + " " + b)	
   
    	
   

def main():
    year = int(input())
    print(zodiac_element(year))


if __name__ == '__main__':
    main()

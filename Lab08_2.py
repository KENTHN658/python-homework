#!/usr/bin/env python3


def classify(list_x):
    list_a = []
    list_b = []
    list_c = []
    for i in list_x:
        b =type(i)
       #rint(b)
        if b == int:
            list_a.append(i)
        elif b == float:
            list_b.append(i)
        elif b == str:
            list_c.append(i)
#print(x1)
#print(x2)
#print(x3)
   

 #เขียนโค้ดลงไปตรงนี้


#ในpython เราสามารถ return ได้มากกว่า 1 ค่า โดยผลลัพธ์จะถูกมัดรวมออกไปเป็นค่าเดียวซึ่งมี type เป็น  Tuple
    return list_a, list_b, list_c

def main():
    x = [10, 'he4>lo', 23.5, 4]
    list_int, list_float, list_string = classify(x)
    print(type(list_int), list_int)
    print(type(list_float), list_float)
    print(type(list_string), list_string)



#<class 'list'> [10, 4]
#<class 'list'> [23.5]
#<class 'list'> ['he4>lo']


if __name__ == '__main__':
    main()
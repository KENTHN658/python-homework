#!/usr/bin/env python3
#!/usr/bin/env python3
# ธนธรณ์ บูญเชิด
# รหัสนักศึกษา 640510658
# Lab 08
# Problem 3
# 204111 Sec 002

'''def main():
    nums = [1,2,3,4]
    nums1 = [1,2,3,4]
    n = int(input())
    nondest_rotate_list(num1,n)'''
    #n = 1
    #print(nums)  #[1, 2, 3, 4]
    #print(nondest_rotate_list(nums, n))   #[4, 1, 2, 3]

    #n = 105
    #print(nums)  #[1, 2, 3, 4]
    #print(nondest_rotate_list(nums, n))  #[4, 1, 2, 3]

    #n = -1
    #print(nums)  #[1, 2, 3, 4]
    #print(nondest_rotate_list(nums, n))  #[2, 3, 4, 1]

def nondest_rotate_list(list_a, n):
    if n>0:
        c = (len(list_a)-1)
        for i in range(n):
            #print("ccccccc")
            list_a = list_a[c:] + list_a[:c]
        return list_a
    elif n<0:
        n = abs(n)
        for i in range(n):
            list_a = list_a[1:] + list_a[:1]
            #print("ccc")
        return list_a
   

def main():
    b = list(input())
    n = int(input())
    nondest_rotate_list(b,n)
    print(nondest_rotate_list(b,n))
    

if __name__ == '__main__':
    main()
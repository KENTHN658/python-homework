def main():
    # รับตัวเลขจาก user
    number = int(input("input number: ")) 
    
    k = int(input('Input digit: '))
    
    # พิมพ์ตัวเลขตำแหน่งที่ k ของข้อมูลเข้า
    print(kth_digit(number, k))

def kth_digit(number, k):
    q = number**2
    w = q**0.5
    g = k**2
    d = g**0.5
    kth = (int(w//(10**d))%10)
    # เขียนโค้ดเพิ่มตรงนี้นะจ๊ะ
    return kth
if __name__ == '__main__':
    main()





    

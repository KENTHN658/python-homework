#!/usr/bin/env python3
# ธนธรณ์ บุญเชิด 
# 640510658
# Lab 06
# Problem 4
# 204111 Sec 002


def main():
    # ด้านล่างเป็นแค่โครงสำหรับการแสดงผล นักศึกษาสามารถเขียนเพิ่มหรือแก้ไขตามความเหมาะสม
    total = int(input("Total students: "))
    x = 0
    ken = 0
    sum_ = 0
    max = 0
    run = 0
    print("Enter score: ")

    for i in range(total):
      x = float(input())
      sum_=sum_+x
      if x > max:
        run = max
        #print(run)
        max = x
        #print(max)
        #sum_ = x + sum_
      elif x > run and x < max:
        run = x
        #sum_ = x + sum_
    
        
      
      
      #sum = x+sum
    if run == 0:
      run = None
    #print(sum_)
    average = sum_/total
    print('---')
    print("Max score is: "+ "%.2f"% max)
    if type(run) == float:
      print("Runner up is: " + "%.2f"%run)
    else:
      print("Runner up is: " + "%s"%run)
      
    print("Average is: " + "%.2f"% average)

if __name__ == '__main__':
    main()

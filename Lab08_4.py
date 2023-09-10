#!/usr/bin/env python3



def dest_rotate_list(nums, n):
    if n>0:
        c = (len(nums)-1)
        for i in range(n):
            nums[:] = nums[c:] + nums[:c]
        #print (nums)
    elif n<0:
        n = abs(n)
        for i in range(n):
            nums[:] = nums[1:] + nums[:1]
        #print (nums)
            #print("ccc")
      
        
        
            
            
    
def main():
   
    n = 1
    nums = [1,2,3,4]
    print(nums)
    out =  dest_rotate_list(nums, n)
    print(out)
    print(nums)
    
   
    n = -2
    nums = [1,2,3,4]
    print(nums)
    out =  dest_rotate_list(nums, n)
    print(out)
    print(nums)
    
   
    n = 105
    nums = [1,2,3,4]
    print(nums)
    out =  dest_rotate_list(nums, n)
    print(out)
    print(nums)
    
    
    
    
    



if __name__ == '__main__':
    main()
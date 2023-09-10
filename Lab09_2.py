import copy
def remove_row_col(list_a, row, col):
    u1 = len(list(list_a))
    #p1 = len(list(list_a[0]))
    #print(p1)
    x1 = copy.deepcopy(list_a)
    if row < u1 and row + u1 >= 0:
      del x1[row]
    
    for i in x1:
        #print(i)
        if len(i) > col and col + len(i) >= 0:
          del i[col]
        
    #print(list_a)
  
    return x1
    
def main():
    x =[[1,2,3,4],
        [5,8],
        [9,10,11,12],
        [13,14,15]]
    row = int(input())
    colrum = int(input())
    print(remove_row_col(x , row , colrum))
    print(x)

    
if __name__ == '__main__':
    main()
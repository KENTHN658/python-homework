#!/usr/bin/env python3
# ธนธรณ์ บุญเชิด
# 640510658
# Quiz2 1/64
# Problem 2b
# 204111 Sec 002

import copy
def transpose_matrix(matrix):
    c = copy.deepcopy(matrix)
    zipped_rows = zip(*c)
    transpose_matrix = [list(row) for row in zipped_rows] 
    #a1 = []
    #for row in  zipped_rows: เหมือนกับ [list(row) for row in zipped_rows] 
        #print(row)
        #a1.append(list(row))
    #print(a1) 
    return transpose_matrix
                #แหล่งที่มา https://www.kite.com/python/answers/how-to-transpose-a-matrix-in-python ณเวลา 11.10

 

def main():

    m_list = [[9]]
    print(m_list)
    print(transpose_matrix(m_list))
    print(m_list)
    m_list = [[0, 2, -3]]
    print(m_list)
    print(transpose_matrix(m_list))
    print()
    m_list = [[-1, 4], [5, 6]]
    print(m_list)
    print(transpose_matrix(m_list))
    print()
    m_list = [[2, -3, 1], [0, 3, 5]]
    print(m_list)
    print(transpose_matrix(m_list))
    print()
    m_list = [[7], [0], [8]]
    print(m_list)
    print(transpose_matrix(m_list))
    print()
    m_list = [[6, 0], [0, -3], [1, 8]]
    print(m_list)
    print(transpose_matrix(m_list))
    print()

    # test cases
    m_list = [[7, -9, 0]]
    print(m_list)
    print(transpose_matrix(m_list))
    m_list = [[4, -1, 5], [3, 0, -2]]
    print(m_list)
    print(transpose_matrix(m_list))
    m_list = [[0], [0], [7]]
    print(m_list)
    print(transpose_matrix(m_list))
    m_list = [[5, -1], [-1, -2], [6, -3]]
    print(m_list)
    print(transpose_matrix(m_list))
    m_list = [[-8, -2], [0, 0]]
    print(m_list)
    print(transpose_matrix(m_list))
    m_list = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]]
    print(m_list)
    print(transpose_matrix(m_list))
    m_list = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(m_list)
    print(transpose_matrix(m_list))


if __name__ == '__main__':
    main()

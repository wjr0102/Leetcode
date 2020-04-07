#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-12-17 19:47:45
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2020-04-07 10:15:00
import numpy as np

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i = 0
        # Total n%2 layer
        while i <= n//2-1:
            # Move n-2*i items
            j = 0
            x = i
            while j<n-2*i-1:
                # Move 4 items
                y = j+i
                num = matrix[x][y]
                for k in range(4):
                    # print(i,j,k)
                    # print("Origin: (%d,%d)\r num: %d"%(x,y,num))
                    py = n - x - 1
                    px = y
                    temp = matrix[px][py]
                    matrix[px][py] = num
                    num = temp
                    x = px
                    y = py
                    # print("After: (%d,%d)\r num: %d"%(x,y,num))
                    # print(matrix)
                j += 1
            i += 1



def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    # Change the type of matrix
    #matrix = np.array(matrix)
    # [right, down, left, up]
    directions = [np.array([0, 1]), np.array(
        [1, 0]), np.array([0, -1]), np.array([-1, 0])]
    n = len(matrix)
    last_cor = np.array([-1, -1])
    for i in range(n - 1, n % 2, -2):
        # Step span i
        # print("STEP SPAN: %d" % i)
        cor = last_cor + np.array([1, 0])
        last_cor = cor
        for j in range(i):
            # Position j
            # print("Position j: %d" % j)
            cor[1] = cor[1] + 1
            current = matrix[cor[0]][cor[1]]
            # print("Current (x,y): %s" % (str)(cor))
            # print("Current value: %d" % current)
            for k in range(4):
                # Diriction k
                dir1 = i - j
                dir2 = j
                direction = dir1 * directions[k] + \
                    dir2 * directions[(k + 1) % 4]
                cor = cor + direction
                # print("Next (x,y):%s" % (str)(cor))
                # The item will be replaced
                temp = matrix[cor[0], cor[1]]
                # print("Next value: %d" % temp)
                matrix[cor[0], cor[1]] = current
                current = temp
                # print(matrix)
    print(matrix)


if __name__ == "__main__":
    l = range(1, 26)
    l = np.array(l)
    l = l.reshape((5, 5))
    print(rotate(l))

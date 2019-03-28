#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-28 15:28:28
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-28 16:52:32


def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    matrix = [[0 for i in range(n)] for i in range(n)]
    width = n
    num = 1
    while width > 0:
        print(width)
        start = (n - width) // 2
        # if (width == 1):
        #     matrix[start][start] = num
        #     return matrix
        # Right
        print("Right")
        for j in range(start, start + width):
            matrix[start][j] = num
            num += 1
            showMatrix(matrix)
        # Down
        print("Down")
        for j in range(start + 1, start + width):
            matrix[j][start + width - 1] = num
            num += 1
            showMatrix(matrix)
        # Left
        print("Left")
        for j in range(start + width - 2, start - 1, -1):
            matrix[start + width - 1][j] = num
            num += 1
            showMatrix(matrix)
        # Up
        print("Up")
        for j in range(start + width - 2, start, -1):
            matrix[j][start] = num
            num += 1
            showMatrix(matrix)
        width = width - 2

    return matrix


def showMatrix(matrix):
    for row in matrix:
        print(row)
    print()


if __name__ == "__main__":
    showMatrix(generateMatrix(5))

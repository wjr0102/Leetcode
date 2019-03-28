#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-28 16:53:30
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-28 17:45:11


def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    print(matrix)
    if not matrix:
        return None
    result = []
    rows = len(matrix)
    if rows == 1:
        return matrix[0]
    cols = len(matrix[0])
    if cols == 1:
        for nums in matrix:
            result.append(nums[0])
        return result
    width = cols
    height = rows
    while width > 0 and height > 0:
        col_start = (cols - width) // 2
        row_start = (rows - height) // 2

        print(row_start, col_start)
        print("Right")
        # Right
        for num in matrix[row_start][row_start:row_start + width]:
            result.append(num)

        print(result)

        print("Down")
        # Down
        for nums in matrix[col_start + 1:col_start + height]:
            result.append(nums[row_start + width - 1])

        print(result)

        print("Left")
        # Left
        for num in matrix[col_start + height - 1][row_start + width - 2:row_start:-1]:
            result.append(num)

        print(result)

        if width == 1:
            break

        print("Up")
        # Up
        for nums in matrix[col_start + height - 1:col_start:-1]:
            result.append(nums[col_start])

        print(result)

        width -= 2
        height -= 2

    return result


def spiralOrder2(matrix):
    M = [[False for i in range(len(matrix[0]))] for i in range(len(matrix))]
    # Right


if __name__ == "__main__":
    print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

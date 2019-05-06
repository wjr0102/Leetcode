#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-04-04 13:24:21
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-04-04 19:23:56

'''
        G(i) = i ^ (i/2);
        如 n = 3: 
        G(0) = 000, 
        G(1) = 1 ^ 0 = 001 ^ 000 = 001
        G(2) = 2 ^ 1 = 010 ^ 001 = 011 
        G(3) = 3 ^ 1 = 011 ^ 001 = 010
        G(4) = 4 ^ 2 = 100 ^ 010 = 110
        G(5) = 5 ^ 2 = 101 ^ 010 = 111
        G(6) = 6 ^ 3 = 110 ^ 011 = 101
        G(7) = 7 ^ 3 = 111 ^ 011 = 100
'''


def grayCode(n):
    """
    :type n: int
    :rtype: List[int]
    """
    res = [0]
    for i in range(1, 2**n):
        res.append(i ^ (i // 2))
    return res


def grayCode2(n):
    """
    :type n: int
    :rtype: List[int]
    """
    dic = {}
    dic[0] = [[0 for i in range(n)]]
    for i in range(1, n + 1):
        print(i - 1, dic[i - 1])
        dic[i] = dic[i - 1] + extend(dic[i - 1])
        print(i - 1, dic[i - 1])
        print(i, dic[i])
    return dic[n]


def extend(nums):
    res = []
    for i in range(len(nums) - 1, -1, -1):
        new = nums[i][:]
        i = 0
        while new[i] == 0 and i < len(new):
            i += 1
            if i >= len(new):
                break
        new[i - 1] = 1
        res.append(new)
    print(res)
    return res


if __name__ == "__main__":
    print(grayCode2(2))

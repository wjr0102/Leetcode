#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-04-02 00:34:53
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-04-02 00:53:20

'''
f(n) = f(n-1) + f(n-2)

1: 1
2: 1+1 = 2
3: 2+1 = 3
4: 3+1 = 4 111+1 11+2 12+1 21+1 2+2
'''


def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """

    result[1] = 1
    result[2] = 2
    for i in range(3, n + 1):
        result[i] = result[i - 1] + result[i - 2]

    return result[n]

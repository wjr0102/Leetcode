#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-29 20:10:25
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-29 20:14:48


def isPowerOfTwo(self, n):
    """
    :type n: int
    :rtype: bool
    """
    if n == 0:
        return False
    while n % 2 == 0:
        n = n // 2
    if n == 1:
        return True
    else:
        return False

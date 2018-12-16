#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-12-16 20:06:21
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-12-16 20:48:37
import math


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """

    if x < 0:
        return False
    if x == 0:
        return True
    # 判断有几位
    bits = (int)(math.log10(x) + 1)
    if bits == 1:
        return True
    # 位数为偶数
    if bits % 2 == 0:
        left_mid = bits // 2 + 1
        right_mid = bits // 2
    else:
        left_mid = bits // 2 + 2
        right_mid = bits // 2
    while right_mid != 0:
        left = (x % math.pow(10, left_mid)) // math.pow(10, left_mid - 1)
        right = (x % math.pow(10, right_mid)
                 ) // math.pow(10, right_mid - 1)
        print left_mid, right_mid
        print left, right
        if left != right:
            return False
        else:
            left_mid += 1
            right_mid -= 1

    return True


if __name__ == "__main__":
    print(isPalindrome(1234321))

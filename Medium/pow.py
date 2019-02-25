#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-12-17 18:16:05
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-12-17 18:38:54


def myPow(x, n):
    if n < 0:
        n = -n
        x = 1.0 / x
    result = 1
    tmp = x
    if n % 2 == 1:
        result = result * tmp
    n = n // 2
    while (n > 0):
        tmp = tmp * tmp
        if n % 2 == 1:
            result = result * tmp
        n = n // 2
    return result


def toBinary(n):
    a = n
    result = []
    while a // 2 > 0:
        result.append(a % 2)
        a = a // 2
    result.append(a % 2)
    # result.reverse()
    return result


if __name__ == "__main__":
    print(myPow(2.0, 10))

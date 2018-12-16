#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-12-16 20:51:01
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-12-16 21:11:44


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
           'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    result = 0
    i = 0
    while i < len(s):
        if i == len(s) - 1:
            result += dic[s[i]]
            return result
        current = s[i:i + 2]
        if dic.has_key(current):
            result += dic[current]
            i += 2
        else:
            result += dic[current[0]]
            i += 1
        #print result
    return result


if __name__ == "__main__":
    print(romanToInt('DCXXI'))

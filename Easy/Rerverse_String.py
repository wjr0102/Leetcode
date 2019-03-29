#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-29 18:07:11
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-29 18:10:24


def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    for i in range(len(s) // 2):
        temp = s[i]
        s[i] = s[len(s) - i - 1]
        s[len(s) - i - 1] = temp
        print(s)


if __name__ == "__main__":
    s = ['h', 'e', 'l', 'l', 'o']
    reverseString(s)
    print(s)

#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-12-17 15:26:58
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-12-17 15:48:58


def myatoi(s):
    # Delete whitespace
    INT_MIN = -2147483648
    INT_MAX = 2147483647
    s = s.strip()
    print s
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(s) == 0:
        return 0
    if not (s[0] in numbers or s[0] == '-' or s[0] == '+'):
        return 0
    else:
        i = 1
        while i < len(s) and s[i] in numbers:
            i += 1
        s = s[:i]
        if (len(s) == 1) and (s[0] in {"-", "+"}):
            return 0
        s = (int)(s)
        if s > INT_MAX:
            s = INT_MAX
        elif s < INT_MIN:
            s = INT_MIN
    return s


if __name__ == "__main__":
    print(myatoi("   +"))

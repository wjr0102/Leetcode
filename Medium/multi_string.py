#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-04-13 23:41:49
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-04-14 00:42:25


def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    len1 = len(num1)
    len2 = len(num2)
    result = ""
    if len1 > len2:
        temp = num1
        num1 = num2
        num2 = temp
        len1 = len(num1)
        len2 = len(num2)

    count = 0
    for i in range(len1 - 1, -1, -1):
        last_result = result
        result = ""
        print("First:%s" % num1[i])
        c = 0
        for j in range(len2 - 1, -1, -1):
            print("Second:%s" % num2[j])
            s = (int)(num1[i]) * (int)(num2[j]) + c
            c = s // 10
            s = s % 10
            result += (str)(s)
        if c != 0:
            result += (str)(c)
        result = "".join('0' for i in range(count)) + result
        result = add(last_result, result)
        print(result)
        count += 1

    return result[::-1]


def add(s1, s2):
    print("Add\n %s\t%s" % (s1, s2))
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        temp = s1
        s1 = s2
        s2 = temp
        len1 = len(s1)
        len2 = len(s2)

    c = 0
    result = ""
    for i in range(len1):
        s = (int)(s1[i]) + (int)(s2[i]) + c
        c = s // 10
        s = s % 10
        result += (str)(s)
    if len1 != len2:
        print("LENGTH")
        for i in range(len1, len2):
            s = (int)(s2[i]) + c
            print(s)
            c = s // 10
            s = s % 10
            print(s, c)
            result += (str)(s)
    if c != 0:
        result += (str)(c)
    return result


if __name__ == '__main__':
    print(multiply("999", "999"))

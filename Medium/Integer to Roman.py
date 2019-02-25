#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-12-17 00:06:23
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-12-17 00:38:15

# Input range: [1,3999]


def intToRoman2(num):
    # divide the number
    thousand = num // 1000
    hundred = (num // 100) % 10
    ten = (num // 10) % 10
    one = num % 10
    dic = {1: {0: "I", 1: "X", 2: "C", 3: "M"}, 5: {0: "V", 1: "L", 2: "D"}, 4: {
        0: "IX", 1: "XL", 2: "CD"}, 9: {0: "IX", 1: "XC", 2: "CM"}}
    l = [thousand, hundred, ten, one]
    result = ""
    for i in range(len(l)):
        # print l[i]
        j = 3 - i
        if dic.has_key(l[i]):
            result += dic[l[i]][j]
        else:
            if l[i] > 5:
                result += dic[5][j]
                l[i] -= 5
                result += dic[1][j] * l[i]
            else:
                result += dic[1][j] * l[i]
    return result


def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    # divide the number
    thousand = num // 1000
    hundred = (num // 100) % 10
    ten = (num // 10) % 10
    one = num % 10
    # print thousand, hundred, ten, one
    result = ""
    while thousand > 0:
        result += "M"
        thousand -= 1
    while hundred > 0:
        if hundred == 9:
            result += "CM"
            hundred -= 9
        elif hundred >= 5:
            result += "D"
            hundred -= 5
        elif hundred == 4:
            result += "CD"
            hundred -= 4
        else:
            result += "C"
            hundred -= 1
    while ten > 0:
        if ten == 9:
            result += "XC"
            ten -= 9
        elif ten == 4:
            result += "XL"
            ten -= 4
        elif ten >= 5:
            result += "L"
            ten -= 5
        else:
            result += "X"
            ten -= 1
    while one > 0:
        if one == 9:
            result += "IX"
            one -= 9
        elif one == 4:
            result += "IV"
            one -= 4
        elif one >= 5:
            result += "V"
            one -= 5
        else:
            result += "I"
            one -= 1
    return result


if __name__ == "__main__":
    print(intToRoman(4))
    print(intToRoman2(4))

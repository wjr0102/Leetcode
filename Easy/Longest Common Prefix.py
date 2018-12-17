#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-12-17 15:49:21
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-12-17 16:40:26
import time


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return ""
    result = ""
    strs = sorted(strs, key=lambda item: len(item))
    for i in range(1, len(strs[0]) + 1):
        result = strs[0][:i]
        for item in strs:
            if item[:i] != result:
                return result[:-1]
    return result


def longestCommonPrefix_2(strs):
    if len(strs) == 0:
        return ""
    strs = sorted(strs, key=lambda item: len(item))
    result = strs[0]
    last = is_leagal(result, strs)
    if last:
        return result
    right = len(result)
    mid = right //2
    mid_last = -1
    print last
    while mid != mid_last:
        current = is_leagal(result[:mid],strs)
        print current
        if current:
            mid_last = mid
            mid = (mid + right)//2
        else:
            right = mid
            mid_last = mid
            mid = mid //2
        print ("result = %s\nleft = %s\nright = %s"%(result, result[:mid], result[mid:]))


    return result[:mid]


def is_leagal(result, strs):
    print("Is \'%s\'' Legal?" % result)
    for item in strs:
        if item.find(result) != 0:
            return False
    return True


if __name__ == "__main__":
    print(longestCommonPrefix_2(["abab", "aba", "abc"]))

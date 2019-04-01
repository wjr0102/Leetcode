#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-29 21:10:12
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-29 21:22:10


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dic = {}
    for num in nums:
        if dic.__contains__(num):
            dic[num] += 1
        else:
            dic[num] = 1
    result = sorted(dic.items(), key=lambda x: x[1])
    return result[-1][0]


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dic = {}
    max_value = -1
    result = -1
    for num in nums:
        if dic.__contains__(num):
            dic[num] += 1
        else:
            dic[num] = 1
        if dic[num] > max_value:
            max_value = dic[num]
            result = num
    return result

'''
摩尔投票法证明：
因为出现次数>n/2，所以必会大于0
'''

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    cnt = 0
    for num in nums:
        if cnt == 0:
            res = num
        elif num != res:
            cnt -= 1
        else:
            cnt += 1

    return res

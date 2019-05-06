#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-04-02 11:36:04
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-04-04 19:35:58


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 2:
        return [nums]

    dic = {}
    dic[0] = [[nums[0]]]
    for i in range(1, len(nums)):
        dic[i] = extend(dic[i - 1], nums[i])
    return dic[len(nums) - 1]


def extend(numsList, num):
    res = []
    for l in numsList:
        for i in range(len(l) + 1):
            per = l[:]
            per.insert(i, num)
            res.append(per)
    return res


if __name__ == "__main__":
    print(permute([1, 2, 3]))

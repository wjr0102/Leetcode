#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-04-02 00:53:29
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-04-02 00:59:39


def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return None

    res = max(nums)
    if res < 0:
        return res

    res = 0
    subsum = 0
    for num in nums:
        subsum += num
        if subsum < 0:
            subsum = 0
        res = max(res, subsum)

    return res

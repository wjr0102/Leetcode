#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-29 20:37:44
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-29 20:43:19


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    while nums:
        num = nums.pop()
        if num not in nums:
            return num
        else:
            nums.remove(num)
'''
# xor
        a = 0
        for num in nums:
            a ^= num
        return a
'''


if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]

#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-29 18:39:23
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-29 18:58:52


def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    zero_num = 0
    zero_list = []
    while 0 in nums:
        zero_num += 1
        zero_list.append(nums.index(0))
        nums[nums.index(0)] = 1

    result = 1
    for num in nums:
        result = result * num

    results = None
    if zero_num == 1:
        results = [0 for i in range(len(nums))]
        results[zero_list[0]] = result
    elif zero_num > 1:
        results = [0 for i in range(len(nums))]
    else:
        result = [result // num for num in nums]
    return results


def productExceptSelf2(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    lefts = [1]
    rights = [1]
    for i in range(len(nums)):
        lefts.append(lefts[-1] * nums[i])
        rights.append(rights[-1] * nums[len(nums) - i - 1])
    results = []

    for i in range(len(nums)):
        results.append(lefts[i] * rights[len(nums) - i - 1])

    return results


def productExceptSelf3(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    results = [1 for i in range(len(nums))]
    left = 1
    right = 1
    for i in range(len(nums)):
        results[i] *= left
        left *= nums[i]
    for j in range(len(nums)):
        results[len(nums) - i - 1] *= right
        right *= nums[len(nums) - i - 1]

    return results

#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-12-27 20:09:21
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-12-27 21:30:41
result = 100000000


def minMove2(nums):
    nums = sorted(nums)
    middle = nums[len(nums) // 2]
    result = sum([abs(num - middle) for num in nums])
    return result


if __name__ == "__main__":
    print(minMove2([1, 2, 3, 4]))

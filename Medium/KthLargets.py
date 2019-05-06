#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-04-12 14:14:26
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-04-12 20:17:09

# 快排


def findKthLargest(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    if not num or len(num) < k:
        return None

    num = nums[0]
    left, right = 0


def findKthLargest(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    index = self.find(nums, 0, len(nums) - 1)
    if index > k:
        index = self.find(nums, 0, index - 1)
    elif index < k:
        index = self.find(nums, index + 1, len(index) - 1)
    else:
        return nums[index]


def find(self, nums, left, right):
    num = nums[0]
    l = left
    r = right
    while(l < r):
        while l < r and nums[r] <= num:
            r -= 1
        temp = nums[r]
        nums[r] = nums[l]
        nums[l] = temp
        while l < r and nums[l] >= num:
            l += 1
        temp = nums[r]
        nums[r] = nums[l]
        nums[l] = temp
    return l

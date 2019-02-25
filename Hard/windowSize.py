#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-12-17 00:42:49
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-12-17 15:30:24
import collections

def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if len(nums)==0 or k==0:
        return []
    maxs = []
    for i in range(len(nums)-k+1):
        maxs.append(max(nums[i:k+i]))
    return maxs

def maxSlidingWindow2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    q = collections.deque()
    maxs = []
    for i in range(len(nums)):
        while q and nums[q[-1]]<nums[i]:
            q.pop()

        q.append(i)

        if i - q[0]>=k:
            q.popleft()

        if i+1 >=k:
            maxs.append(nums[q[0]])

    return maxs

if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    result = maxSlidingWindow2(nums,k)
    print(result)
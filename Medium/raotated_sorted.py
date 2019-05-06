#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-04-13 17:22:10
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-04-13 22:45:13


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2
    last = nums[left]
    count = 0
    while not check_mid(nums, mid) and count < len(nums):
        count += 1
        print("Left: %d\t Right: %d\t Mid: %d\n %d,%d" %
              (left, right, mid, nums[mid], last))

        if nums[mid] > last:
            left = mid + 1
        else:
            right = mid - 1
        print("Left: %d\t Right: %d" % (left, right))
        last = nums[mid]
        mid = (left + right) // 2

    phase = mid
    if count >= len(nums):
        phase = 0
    print(phase)
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2
    mid_index = index_change(mid, phase, len(nums))
    while left <= right:
        print("Left: %d\t Right: %d" % (left, right))
        if target < nums[mid_index]:
            right = mid - 1
        elif target > nums[mid_index]:
            left = mid + 1
        else:
            return mid_index

        mid = (left + right) // 2
        mid_index = index_change(mid, phase, len(nums))

    if nums[mid_index] != target:
        return -1

    return mid_index


def check_mid(nums, mid):
    if mid - 1 < 0:
        return (nums[mid + 1] > nums[mid])
    if mid + 1 >= len(nums):
        return (nums[mid] < nums[mid - 1])
    return (nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1])


def index_change(ranked, phase, length):
    print("Rank:%d\tPhase:%d\tLength:%d" % (ranked, phase, length))
    return (ranked + phase) % length


if __name__ == "__main__":
    nums = [2, 3, 7, 8, 1]
    target = 5
    print(search(nums, target))

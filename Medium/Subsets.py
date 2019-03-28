#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-28 15:12:21
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-28 15:25:07


def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = [[]]
    for num in nums:
        print(result)
        print(num)
        for i in range(len(result)):
            new_subset = result[i][:]
            new_subset.append(num)
            print(new_subset)
            result.append(new_subset)
    return result


def subsets2(nums):

    result = [[]]
    for num in nums:
        result += [j + [num] for j in result if j] + [[num]]
    return result


if __name__ == "__main__":
    print(subsets([1, 2, 3]))

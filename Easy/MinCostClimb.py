#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-05-07 01:46:49
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-05-07 01:53:03

'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:

Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:

Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
'''
import sys


def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    result = [sys.maxsize for i in range(len(cost))]
    result[0] = cost[0]
    result[1] = min(cost[0], cost[1])
    for i in range(2, len(cost)):
        result[i] = min(result[i - 1], result[i - 2] + cost[i])
    return result[len(cost) - 1]

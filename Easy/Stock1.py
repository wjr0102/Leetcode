#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-04-01 23:33:01
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-04-02 00:17:34
import sys


def maxProfit(prices):
    if not prices:
        return 0

    buy = prices[0]
    profit = 0
    for i in range(len(prices)):
        buy = min(prices[i], buy)
        profit = max(prices[i] - profit, profit)
    return profit


def maxProfit(prices):
    if len(prices) < 2:
        return 0

    buy = sys.maxint
    profit = 0
    for i in range(len(prices)):
        buy = min(prices[i], buy)
        if prices[i] - buy > 0:
            profit += prices[i] - buy
            buy = prices[i]

    return profit

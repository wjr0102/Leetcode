#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2020-04-02 22:33:10
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2020-04-02 22:33:16

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for i in range(amount+1)]
        dp[0] = 0
        for i in range(1,amount+1):
            res = -1
            for coin in coins:
                if i-coin>=0:
                    if dp[i-coin]>=0:
                        res = dp[i-coin]+1
                        if dp[i]<0 or res<dp[i]:
                            dp[i] = res
        #print(dp)
        return dp[amount]
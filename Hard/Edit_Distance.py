#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-02-25 20:04:41
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-02-27 16:38:20

import numpy as np
'''
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
'''


def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    # Initialize the dp matrix
    dp = np.zeros((len(word1), len(word2)))
    if (word1[0] != word2[0]):
        dp[0, 0] = 1
    # Initialize the dp[i,0]
    for i in range(1, len(word1)):
        dp[i, 0] = dp[i - 1, 0] + 1
    print(dp)


if __name__ == "__main__":
    word1 = 'horse'
    word2 = 'ros'
    minDistance(word1, word2)

#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-02-25 20:04:41
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2020-04-06 22:39:53

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
    is_found = False
    dp = np.zeros((len(word1), len(word2)))
    if (word1[0] != word2[0]):
        dp[0, 0] = 1
    else:
        is_found = True
    # Initialize the dp[i,0]
    for i in range(1, len(word1)):
        if word1[i] != word2[0]:
            dp[i, 0] = dp[i - 1, 0] + 1
        elif not is_found:
            dp[i,0] = dp[i-1,0]
            is_found = True
        else:
            dp[i,0] = dp[i-1,0]+1
    # Initialize the dp[0,i]
    for i in range(1,len(word2)):
        dp [0,i] = dp[0,i-1] + 1
        if word1[0]==word2[i]:
            dp[0,i] = dp[0,i] - 1
    for i in range(1,len(word1)):
        for j in range(1,len(word2)):
            if word1[i] != word2[j]:
                dp[i,j] = min(dp[i-1,j-1],dp[i-1,j],dp[i,j-1]) + 1
            else:
                dp[i,j] = min(dp[i-1,j-1],dp[i-1,j]+1)
    print(dp)
    return(dp[len(word1)-1,len(word2)-1])


if __name__ == "__main__":
    word1 = 'pneumonoultramicroscopicsilicovolcanoconiosis'
    word2 = 'ultramicroscopically'
    # word1 = "sea"
    # word2 = "eat"
    minDistance(word1, word2)

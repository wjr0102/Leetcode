#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-08-31 18:33:12
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-08-31 18:43:56

'''
Input:
    queries, words
Output:
    The number of words with less f(frequency) than queries.

Funtion: f(frequency)
    The frequency of the smallest character
'''


class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        freq_q = []
        freq_w = []
        ans = [0 for i in range(queries)]
        # Get the frequency of the queries
        for query in queries:
            freq_q.append(getFrequency(query))
        for word in words:
            freq_w.append(getFrequency(word))
        for i in range(queries):
            for j in range(words):
                if freq_w[j] > freq_q[i]:
                    ans[i] += 1
        return ans

    def getFrequency(self, word):
        """
        Find the frequency of the smallest character.

        :type words: str
        :rtype: int
        """

        # if word is empty then return 0
        if not word:
            return 0

        # while word is not empty
        ch = word[0]    # choose the first character as the samllest one
        freq = 1    # the frequency of ch
        for c in word[1:]:
            if c < ch:
                ch = c
                freq = 1
            elif c == ch:
                freq += 1

        return freq

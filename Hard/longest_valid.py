#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-04-14 16:50:04
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-04-17 22:09:09


def longestValidParentheses(self, s):
    """
    :type s: str
    :rtype: int
    """
    stack = []
    for i in range(len(s)):
        if s[i]=='(':
            stack.append()

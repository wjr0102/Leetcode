#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-04-02 00:19:35
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-04-02 00:26:09


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        x = self.stack.pop()
        if self.min_stack and x in self.min_stack:
            self.min_stack.remove(x)

    def top(self):
        """
        :rtype: int
        """
        return self.stack.pop()

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

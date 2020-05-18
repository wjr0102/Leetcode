#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-04-02 00:19:35
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2020-05-12 10:18:12

'''
    辅助栈（用以保存后进来的较小值）
'''

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
        if self.min_stack and x == self.min_stack[-1]:
            self.min_stack.pop()

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


'''
    不用额外的栈
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_num = None


    def push(self, x: int) -> None:
        if not self.stack:
            self.min_num = x
        elif self.min_num >= x:
            self.stack.append(self.min_num)
            self.min_num = x
        self.stack.append(x)
            


    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min_num:
            if self.stack:
                self.min_num = self.stack.pop()
        


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_num



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

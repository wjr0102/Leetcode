#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-29 22:01:08
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-29 22:10:07


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.stack = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.cache.__contains__(key):
            self.stack.remove(key)
            self.stack.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if (len(self.cache) == self.capacity) and (not self.cache.__contains__(key)):
            delete_key = self.stack.pop(0)
            del(self.cache[delete_key])

        self.cache[key] = value
        self.stack = self.cache.keys()

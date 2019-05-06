#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-04-02 01:22:51
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-04-02 01:22:59
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while i < m and j < n:
            print(i, nums1[i], j, nums2[j])
            if nums2[j] < nums1[i]:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1

            i += 1
            print(nums1)
        if j < n:
            for k in range(i + j, n + m):
                nums1[k] = nums2[k - i]

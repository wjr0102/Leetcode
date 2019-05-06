#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-04-13 23:10:03
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-04-13 23:17:20


def uniquePaths(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    map_array = [[0 for i in range(m)] for i in range(n)]
    for i in range(m):
        map_array[0][i] = 1
    for j in range(n):
        map_array[j][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            map_array[i][j] = map_array[i][j - 1] + map_array[i - 1][j]

    return map_array[n][m]

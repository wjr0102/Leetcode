#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2020-04-03 17:23:48
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2020-04-03 17:41:56
'''
    模拟
'''
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        l = list(range(n))
        k = 0
        while len(l)>1:
            k = (k+m-1)%len(l)
            l.pop(k)
        return l[0]

'''
    数学:
    令f(N,M)表示为总共有N人，报到第M人出局时胜利者的在该轮次的索引
    则，f(1,M) = 0
        f(2,M) = (f(1,M)+M)%2
        f(3,M) = (f(2,M)+M)%3
        ...
        f(N,M) = (f(N-1,M)+M)%N
'''
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        dic = {1:0}
        for i in range(2,n+1):
            dic[i] = (dic[i-1]+m)%i 
        return dic[n]
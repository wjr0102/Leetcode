#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-12-17 18:05:17
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-12-17 18:19:50
import itertools


def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    dic = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": [
        "m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
    # print list(itertools.product(dic["2"], dic["3"],dic["4"]))
    result = []
    for i in range(len(digits)):
        s = ""


if __name__ == "__main__":
    letterCombinations("23")

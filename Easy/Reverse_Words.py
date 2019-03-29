#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-29 18:13:31
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-29 18:21:22


def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    s += " "
    result = ""
    word = []
    for c in s:
        if c != ' ':
            word.append(c)
        else:
            result += reverseString(word)
            result += " "
            word = []

    return result[:-1]


def reverseString(word):
    head = 0
    tail = len(word) - 1
    while head < tail:
        word[head], word[tail] = word[tail], word[head]
        head += 1
        tail -= 1

    return ''.join(word)


if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    print(reverseWords(s))

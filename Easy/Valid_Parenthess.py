#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-28 17:47:52
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-28 17:59:05


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) % 2 != 0:
        return False

    stack = []
    dic = {'(': ')', '[': ']', '{': '}'}
    # Deal with '(','[','{'
    for char in s:
        if dic.__contains__(char):
            stack.append(char)
        else:
            if stack:
                p = stack.pop()
                if char != dic[p]:
                    return False
            else:
                return False

    if stack:
        return False
    else:
        return True


if __name__ == "__main__":
    print(isValid("()"))

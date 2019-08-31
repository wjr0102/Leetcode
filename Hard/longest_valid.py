#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-04-14 16:50:04
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-06-16 18:45:58


def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    stack = []
    result = 0
    current = 0
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(s[i])
        else:
            # stack为空,不合法
            if (not stack): 
                if (current > result):
                    result = current
                    current = 0
            else:
                current += 2
                stack.pop(-1)
                print(stack)
        print("result = %d\t current = %d"%(result,current))

    if current > result:
        result = current
    return result

if __name__ == "__main__":
    s = "()(()"
    print(longestValidParentheses(s))

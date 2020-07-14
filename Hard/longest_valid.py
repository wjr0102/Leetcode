#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-04-14 16:50:04
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2020-07-05 16:54:18

'''
    32. 最长有效括号
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
            dp,dp[i]是以i为最后一个字符时，最长的长度

            如果是"(",则dp[i]=0
            如果是")",则
                - 如果前一个是"(",则dp[i] = dp[i-2]+2
                - 如果前一个是")",则
                    - 如果有和它匹配的括号，即s[i-dp[i-1]-1]="("
                        dp[i] = dp[i-1]+2
                        - 再加上前面"("有效括号长度，即
                            dp[i] += dp[i-dp[i-1]-2]
        """
        if not s:
            return 0
        dp = [0]*len(s)
        l = 0
        for i in range(len(s)):
            if s[i]==")":
                if i-1>=0:
                    # ()
                    if s[i-1]=="(":
                        if i-2>=0:
                            dp[i] = dp[i-2]+2
                        else:
                            dp[i] = 2
                    # ...))
                    else:
                        index = i - dp[i-1]-1
                        if index >=0 and s[index]=="(":
                            dp[i] = dp[i-1]+2
                            if index-1>=0:
                                dp[i] += dp[index-1]
        return max(dp)


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
            将"("的索引压入栈内，初始为"-1"

            当有未匹配的")"时，将其索引压入栈内
        """
        res = 0
        ans = 0
        stack = [-1]
        for i in range(len(s)):
            c = s[i]
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    index = stack[-1]
                    res = i - index
                    ans = max(res,ans)
                else:
                    stack.append(i)
        return ans

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        res = 0

        for c in s:
            if right == left:
                res = max(res,left*2)
            if right > left:
                left = 0
                right = 0
            if c=="(":
                left += 1
            if c==")":
                right += 1
            print(left,right)
        if right == left:
            res = max(res,left*2)
            
        left = 0
        right = 0
        
        for i in range(len(s)-1,-1,-1):
            c = s[i]
            if right == left:
                res = max(res,left*2)
            if left > right:
                left = 0
                right = 0
            if c=="(":
                left += 1
            if c==")":
                right += 1
            # print(left,right)

        return res



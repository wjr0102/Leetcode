#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-12-17 00:42:49
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-12-17 15:30:24
import re


def isp_legal(p):
    print("Is p leagal")
    print p
    index = p.find("*")
    p_next = p
    i = 0
    while (index != len(p_next) - 1) and (index != -1):
        print p_next, index
        p_next = p_next[index + 1:]
        index = p_next.find("*")
        # print p_next
        i += 1
    if len(p_next) - 1 == index:
        return 1
    else:
        return -1


def isMatch_start(s, p):
    print("--------With * match--------")
    print("String = %s\tPattern = %s\n" % (s, p))
    if len(s) == 0:
        return isp_legal(p)

    if len(p) == 0:
        print "Length of p is 0"
        if len(s) != 0:
            return -1
        else:
            return 1
    index = p.find("*")
    # print(index)
    ''' -1: Not match
        -3: len(p) == len(s) Match
    '''
    if index == -1:
        print("No *")
        status = isMatch_no_star(s, p)
        print ("No *: next_s:%d\tlength:%d\n" % (status, len(s)))
        if status != len(s):
            return -1
    else:
        print("With *")
        p_before = p[:index - 1]
        # print p_before
        next_s = 0
        if len(p_before) != 0:
            next_s = isMatch_no_star(s, p_before)
        if next_s == -1:
            return -1
        elif next_s >= len(s):
            return isp_legal(p[index - 1:])
        else:
            last = p[index - 1]
            print("Last:%s\tNow:%s\t\n" % (last, s[next_s]))
            if last == s[next_s]:
                next_s += 1
                while next_s < len(s):
                    if (s[next_s] == last):
                        next_s += 1
                    else:
                        break
            #print("Last:%s\tNext:%s\t" % (last, s[next_s]))
            if (isMatch_start(s[next_s:], p[index + 1:]) == -1):
                return -1
    return 1


def isMatch_no_star(s, p):
    print("--------With out * match--------")
    print("String = %s\tPattern = %s\n" % (s, p))
    i = 0
    ''' -1: Not match
        -3: len(p) == len(s) Match
    '''
    while (i < len(p)) and (i < len(s)):
        if (s[i] == p[i]) or (p[i] == "."):
            i += 1
        else:
            return -1
    print len(s), len(p), i
    if (i == len(p)):
        return i
    else:
        return -1


def isMatch2(s, p):
    index1 = p.find(".*")
    if index1 != -1:
        p_before = p[:index1]
        if len(p_before) != 0:
            next_s = isMatch_start(s, p_before)
            if next_s == -1:
                return False
            else:
                return True
        else:
            if (len(p[index1 + 2:]) == 0):
                return True
            else:
                for i in range(len(s)):
                    if isMatch2(s[-i:], p[index1 + 2:]) != -1:
                        return True
                return False
    else:
        print("No .*")
        status = isMatch_start(s, p)
        print status
        if status == -1:
            return False
        else:
            return True
    # print p_before


def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    if re.match(p, s) == None:
        return False
    else:
        if (re.match(p, s).span()[1] - re.match(p, s).span()[0]) != len(s):
            return False
        else:
            return True


def isMatch3(s, p):
    global i
    print("The Match Times:%d\ntext:%s\tPattern:%s\n" % (i, s, p))
    i += 1
    if len(p) == 0:
        # Match totally
        if len(s) == 0:
            return True
        # S still has part not matched
        else:
            return False
    # If the first character matched
    match_first = True
    if (len(s) == 0) or ((p[0] != s[0]) and (p[0] != ".")):
        match_first = False
    print(match_first)
    # Is there a "*" in pattern
    if len(p) > 1 and p[1] == "*":
        return (match_first and isMatch3(s[1:], p)) or isMatch3(s, p[2:])
    else:
        if not match_first:
            return match_first
        else:
            return isMatch3(s[1:], p[1:])


def isMatch_dp(s, p):
    '''
    f(i,j) = 
        1. p[j+1] != *, f(i-1,j-1) and s[i]==s[j]
        2. p[j+1] == *,
            2.1 f(i-2,j-2)
            2.2 f(i-1,j) and s[i] == p[j-1]
    '''
    f = {(-1, -1): True}
    for i in range(len(s)):
        f[(i, -1)] = False
    for j in range(len(p)):
        f[(-1, j)] = isp_leagal(p[:j + 1])
        print(p[:j + 1])
    print f
    for i in range(len(s)):
        for j in range(len(p)):
            print i, j, s[i], p[j]
            if (j + 1 < len(p)) and (p[j + 1] != "*") and (p[j] != "*"):
                if p[j] not in {s[i], "."}:
                    return False
                else:
                    f[i, j] = True
            elif p[j] != "*":
                if not (f.has_key((i - 2, j - 2))):
                    f[(i - 2, j - 2)] = False
                if not (f.has_key((i - 1, j + 1))):
                    f[(i - 1, j + 1)] = True
                f[(i, j + 1)] = f[(i - 2, j - 2)
                                  ] or (f[(i - 1, j + 1)] and p[j] in {s[i], "."})
                print(f[(i - 1, j + 1)] and p[j] in {s[i], "."})
                print p[j] in {s[i], "."}
                print f[(i, j + 1)]
                print f
                if not f[(i, j + 1)]:
                    return False
    return True


def isp_leagal(p):
    if len(p) == 0:
        return True
    else:
        index = p.find("*")
        while index != -1:
            p = p[index + 1:]
            index = p.find("*")
        if len(p) != 0:
            return False
        else:
            return True


if __name__ == "__main__":
    i = 1
    print(isMatch_dp("aaa", "a"))

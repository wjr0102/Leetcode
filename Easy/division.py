#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-05-07 01:40:31
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-05-07 01:43:19

'''
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.

e.g 

Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.

Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
'''

def divisorGame(N):
    """
    :type N: int
    :rtype: bool
    """
    return N % 2 == 0

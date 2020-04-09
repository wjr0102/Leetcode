#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2020-04-08 17:36:48
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2020-04-09 19:11:06

class Solution:
    def minimumLengthEncoding(self, words):
        words = set(words)
        flags = set()
        for item in words:
            for i in range(1,len(item)):
                w = item[i:]
                if w in words:
                    flags.add(w)
        ans = 0
        for item in words-flags:
            ans += len(item) + 1
        return ans

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        words = set(words)
        res = {}
        for word in words:
            node = trie.insert(word[::-1])
            res[word] = node
        ans = 0
        for word in res:
            # print(word)
            if not res[word].child:
                ans += len(word) + 1
        return ans

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()


    def insert(self, word: str):
        """
        Inserts a word into the trie.
        """
        # print("Insert %s"%word)
        node = self.root
        for c in word:
            node = node.add(c)
        return node

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c in node.child:
                node = node.child[c]
            else:
                return False
        if node.child:
            return False
        return True


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if c in node.child:
                node = node.child[c]
            else:
                return False
        return True

class Node:
    
    def __init__(self,char=None):
        self.char = char
        self.child = {}

    def add(self,c: str):
        if not self.child.__contains__(c):
            self.child[c] = Node(c)
        return self.child[c]
    
    def show(self):
        print("The node is %s"%self.char)
        print("Children:")
        for c in self.child:
            print(self.child[c].char)

    def show_tree(self):
        self.show()
        for node in self.child:
            self.child[node].show_tree()

    def terminate(self):
        self.child["END"] = 1


if __name__ == "__main__":
    s = Solution()
    words = ["time","me","bell"]
    print(s.minimumLengthEncoding(words))
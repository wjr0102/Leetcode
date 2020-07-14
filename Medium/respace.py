'''
    面试题 17.13. 恢复空格
'''

class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        """
            dp. dp[i]表示长度为i的字符最少未匹配数

            则对于dp[i+1]:
                - s[i]不能匹配: dp[i+1] = dp[i]+1
                - s[i]能匹配:
                    - 找到所有能匹配的单词，开头的idx集合
                        dp[i+1] = min(dp[i+1],dp[idx])
        """
        words = set(dictionary)

        dp = [0]*(len(sentence)+1)
        for i in range(len(sentence)):
            dp[i+1] = dp[i] + 1
            for j in range(i,-1,-1):
                if (sentence[j:i+1] in words):
                    dp[i+1] = min(dp[i+1], dp[j])
        return dp[-1]


"""
    字典树优化
"""
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()


    # 逆序插入
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # print("Insert %s"%word)
        node = self.root
        for i in range(len(word)-1,-1,-1):
            c = word[i]
            node = node.add(c)
        node.terminate()

    def search(self, sentence: str, index: int) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        res = set()
        for i in range(index,-1,-1):
            c = sentence[i]
            if c in node.child:
                node = node.child[c]
                if "END" in node.child:
                    res.add(i)
            else:
                return res
        return res

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

class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        # 字典树
        tree = Trie()
        words = set(dictionary)
        for word in words:
            tree.insert(word)
        
        # dp
        dp = [0]*(len(sentence)+1)

        for i in range(len(sentence)):
            c = sentence[i]
            dp[i+1] = dp[i]+1
            for idx in tree.search(sentence,i):
                dp[i+1] = min(dp[i+1],dp[idx])
        
        return dp[-1]
                

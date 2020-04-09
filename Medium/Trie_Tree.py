class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # print("Insert %s"%word)
        node = self.root
        for c in word:
            node = node.add(c)
        node.terminate()

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
        if "END" in node.child:
            return True
        return False


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
    


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
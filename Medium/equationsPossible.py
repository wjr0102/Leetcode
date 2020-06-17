class Solution:

    class UnionFind:
        def __init__(self):
            # 26个字母的parents
            self.parents = list(range(26))

        def find(self,index):
            # 自成一个集合，和别人没关系
            if self.parents[index] == index:
                return index
            # 更新root
            self.parents[index] = self.find(self.parents[index])
            return self.parents[index]

        def union(self,index1,index2):
            # 更新index1的父辈节点
            self.parents[self.find(index1)] = self.find(index2)

    def equationsPossible(self, equations: List[str]) -> bool:
        uf = Solution.UnionFind()
        for st in equations:
            if st[1] == "=":
                index1 = ord(st[0]) - ord("a")
                index2 = ord(st[3]) - ord("a")
                uf.union(index1, index2)
        for st in equations:
            if st[1] == "!":
                index1 = ord(st[0]) - ord("a")
                index2 = ord(st[3]) - ord("a")
                if uf.find(index1) == uf.find(index2):
                    return False
        return True
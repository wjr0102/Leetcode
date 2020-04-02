class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        stackA = []
        stackB = []
        res = []
        for c in seq:
            if c=="(":
                # 先放B后放A
                if len(stackA)>len(stackB):
                    # 放B
                    stackB.append(c)
                    res.append(1)
                else:
                    # 放A
                    stackA.append(c)
                    res.append(0)
            else:
                # 先匹配A再匹配B
                if len(stackA)>len(stackB):
                    stackA.pop()
                    res.append(0)
                else:
                    stackB.pop()
                    res.append(1)
        return res
import queue
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        q = [root]
        res = [root.val]
        last = root
        parents = {root:-1}
        while q:
            node = q.pop(0)
            if parents[node] == parents[last]:
                res[-1] = node.val
            else:
                res.append(node.val)
                last = node
            if node.left:
                q.append(node.left)
                parents[node.left] = parents[node] + 1
            if node.right:
                q.append(node.right)
                parents[node.right] = parents[node] + 1
        return res
        


if __name__ == "__main__":
    l = [1,2,3,None,5,None,4]
    nodes = []
    for i in range(len(l)):
        if l[i]:
            nodes.append(TreeNode(l[i]))
        else:
            nodes.append(None)
    for node in nodes:
        left = (i+1)*2 - 1
        right = (i+1)*2
        if left<len(l):
            node.left = nodes[left]
            if right<len(l):
                node.right = nodes[right]
    s = Solution()
    s.rightSideView(nodes[0])

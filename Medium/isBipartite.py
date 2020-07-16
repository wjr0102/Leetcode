class Solution:
    def isBipartite(self, graph) -> bool:
        blue = set()
        red = set()
        flags = set()
        n = len(graph)
        total = set([i for i in range(n)])
        while len(flags)!=n:
            diff = total - flags
            queue = [diff.pop()]
            print(flags,diff,queue)
            while queue:
                node = queue.pop()
                flags.add(node)
                print(node)
                for p in graph[node]:
                    if p not in flags:
                        queue.append(p)
                # 染了蓝色
                if node in blue:
                    for p in graph[node]:
                        if p in blue:
                            return False
                        red.add(p)
                # 染了红色
                elif node in red:
                    for p in graph[node]:
                        if p in red:
                            return False
                        blue.add(p)
                # 没染色
                else:
                    is_red = is_blue = False
                    for p in graph[node]:
                        if p in red:
                            is_red = True
                        if p in blue:
                            is_blue = True
                    if is_blue and is_red:
                        return False
                    if is_red:
                        blue.add(node)
                        for p in graph[node]:
                            red.add(p)
                    else:
                        red.add(node)
                        for p in graph[node]:
                            blue.add(p)
        return True
        
if __name__ == "__main__":
    graph =[[2,9],[2,9],[0,1],[5,8],[4,6],[5,7],[6,8],[4,7]]
    s = Solution()
    print(s.isBipartite(graph))

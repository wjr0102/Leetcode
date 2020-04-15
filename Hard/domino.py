# import copy
# class Solution:
#     def domino(self, n: int, m: int, broken) -> int:
#         POS = [(0,1),(1,0),(-1,0),(0,-1)]
#         matrix = [[0 for i in range(m)]for j in range(n)]
#         total = len(broken)
#         for i in range(n):
#             for j in range(m):
#                 if [i,j] not in broken:
#                     is_broken = True
#                     for pos in POS:
#                         if i+pos[0]>=0 and i+pos[0]<n and j+pos[1]>=0 and j+pos[1]<m:
#                             if [i+pos[0],j+pos[1]] not in broken:
#                                 is_broken = False
#                                 break
#                     if is_broken:
#                         matrix[i][j] = -1 
#                         total += broken
#                 else:
#                     matrix[i][j] = -1
#         rest = m*n - total
#         ans = rest // 2
#         if ans==0:
#             return ans
#         POS = {"RIGHT":(0,1),"DOWN":(1,0)}

#         def is_ok(ans,em):
#             if ans==0:
#                 return True
#             empty = copy.deepcopy(em)
#             print("Use %d blocks"%ans)
#             print(empty)
#             ok = False
#             for x in range(n):
#                 for y in range(m):
#                     if empty[x][y]==0:
#                         empty[x][y] = 1
#                         for p in POS:
#                             xn = x+POS[p][0]
#                             yn = y+POS[p][1]
#                             if xn>=0 and xn<n and yn>=0 and yn<m:
#                                 if empty[xn][yn]==0:
#                                     print(p,ans)
#                                     print(empty)
#                                     print(xn,yn)
#                                     empty[xn][yn] = 1
#                                     ok = is_ok(ans-1,empty)
#                                     if ok:
#                                         return True
#                                     empty[xn][yn] = 0
#             return ok

#         while not is_ok(ans,matrix):
#             ans -= 1

#         return ans

class Solution:
    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
        blue = collections.defaultdict(list)
        red = set()
        POS = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(n):
            for j in range(m):
                if [i,j] not in broken and (i,j) not in red:
                    for pos in POS:
                        x = i + pos[0]
                        y = j + pos[1]
                        if x>=0 and x<n and y>=0 and y<m and [x,y] not in broken:
                            blue[(i,j)].append((x,y))
                            red.add((x,y))

        match = {}
        # print(blue)
        # print(red)

        def find(u,v):
            # print(match)
            for r in blue[u]:
                if r in v:
                    continue
                else:
                    v.add(r)
                if r not in match or find(match[r],v):
                    match[r] = u
                    return True
            return False

        for x in blue:
            find(x,set())

        return len(match)
        
if __name__ == "__main__":
    s = Solution()
    n = 2
    m = 3
    broken = [[1,0],[1,1]]
    # broken = [[0, 1], [2, 0], [4, 3], [4, 7], [5, 4]]
    print(s.domino(n,m,broken))
                
import collections
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        dic = collections.defaultdict(int)
        dic[0] = 1
        total = 0
        count = 0
        for x in A:
            total = (total + x)%K
            need = (total-K)%K
            count += dic[need]
            dic[total] += 1
        # print(dic)
        return count
            
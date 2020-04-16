class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        intervals.sort(key=lambda x:x[0])
        ans = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0]>ans[-1][1]:
                ans.append(intervals[i])
            else:
                right = max(ans[-1][1],intervals[i][1])
                ans[-1] = [ans[-1][0],right]
        return ans

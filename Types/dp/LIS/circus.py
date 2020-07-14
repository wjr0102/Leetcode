'''
    面试题 17.08 马戏团人塔
'''
class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        if not height:
            return 0
        people = [0]*len(height)
        for i in range(len(height)):
            people[i] = (height[i],weight[i])
        # 身高相同，体重越重越排在前面
        people.sort(key=lambda x:(x[0],-x[1]))

        def LIS(index):
            tail = [float(inf)]*len(people)
            res = 0
            for stage in people:
                num = stage[index]
                l,r = 0,res
                # print("num=%d"%num)
                while l<=r:
                    m = (l+r)//2
                    # print(l,r,m)
                    if tail[m]<num:
                        l = m + 1
                    else:
                        r = m - 1
                tail[l] = num
                if l==res:
                    res += 1
            return res
        r1 = LIS(1)
        return r1
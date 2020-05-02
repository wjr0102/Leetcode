'''
    归并
'''
# 不用指针
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.ans = 0
        def merge(nums1,nums2):
            # print(nums1,nums2)
            res = [0 for i in range(len(nums1)+len(nums2))]
            i,j = 0,0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    res[i+j] = nums1[i]
                    i += 1
                else:
                    res[i+j] = nums2[j]
                    self.ans = self.ans + len(nums1)-i
                    j += 1
            # print(self.ans)
            if i<len(nums1):
                #self.ans += (len(nums1) - i-1)*len(nums2)
                for k in range(i,len(nums1)):
                    res[k+j] = nums1[k]
            elif j<len(nums2):
                for k in range(j,len(nums2)):
                    res[k+i] = nums2[k]
            # print(res,self.ans)
            return res

        def sort(nums):
            if len(nums) < 2:
                return nums
            middle = len(nums)//2
            left = nums[:middle]
            right = nums[middle:]
            # print(left,right,self.ans)
            l1 = sort(left)
            l2 = sort(right)
            return merge(l1,l2)

        a = sort(nums)
        # print(a)
        return self.ans 
# 用指针
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def sort(l,r):
            if l>=r:
                return 0
            m = (l+r)//2
            ans = sort(l,m) + sort(m+1,r)
            # print(l,r,ans)
            i,j,pos = l,m+1,l
            while i<=m and j<=r:
                if nums[i] <= nums[j]:
                    self.temp[pos] = nums[i]
                    i += 1
                else:
                    self.temp[pos] = nums[j]
                    ans = ans + m-i+1
                    j += 1
                # print(self.temp)
                pos += 1
            for k in range(i,m+1):
                self.temp[pos] = nums[k]
                pos += 1
            for k in range(j,r+1):
                self.temp[pos] = nums[k]
                pos += 1
            nums[l:r+1] = self.temp[l:r+1]
            # print(self.temp)
            # print("nums:")
            # print(nums)
            return ans

        self.temp = [0 for i in range(len(nums))]
        return sort(0,len(nums)-1)   

'''
    树状数组：315 Count Smallers
        - 用树状数组来表示相对排名
        - 从右往左遍历原数组：
            - 每次更新该数字对应的排名的树状数组
            - 计算前缀和
'''
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        class FenwickTree:
            
            def __init__(self,size):
                self.array = [0] * size

            def lowbit(self,m):
                return m&(-m)

            def sumup(self,m):
                ans = 0
                while m>0:
                    ans += self.array[m]
                    m -= self.lowbit(m)
                return ans

            def update(self,x,value):
                while x<len(self.array):
                    self.array[x] += value
                    x += self.lowbit(x)
        
        # 特殊处理
        if not nums:
            return []
        if len(nums)==1:
            return [0]
        
        # 离散化
        s = list(set(nums))
        size = len(s)
        import heapq
        heapq.heapify(s)
        rank_dic = {}
        rank = 1
        for _ in range(size):
            num = heapq.heappop(s)
            rank_dic[num] = rank
            rank += 1

        # 建树
        tree = FenwickTree(size)
        res = [0] * len(nums)

        # Update
        for i in range(len(nums)-1,-1,-1):
            rank = rank_dic[nums[i]]
            tree.update(rank,1)
            res[i] = tree.sumup(rank-1)

        return res    
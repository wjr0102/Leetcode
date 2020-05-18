'''
    前缀和.
    对于满足和为k的子序列'i...j': pre[j]-pre[i-1] = k
    即，pre[i-1] = pre[j] - k
'''
import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = collections.defaultdict(int)  # 存储前缀和出现的次数
        total = 0   # 保存当前前缀和
        count = 0   # 保存结果
        dic[0] = 1  # 和为0的前缀和出现了1次（即长度为0）
        # 遍历数组
        for num in nums:
            # 更新前缀和
            total += num
            # 计算pre[i-1]
            need = total - k
            # 更新次数，加上满足和为need的前缀和出现的次数
            count += dic[need]
            # 更新和为total的前缀和出现的次数
            dic[total] += 1
        return count

            
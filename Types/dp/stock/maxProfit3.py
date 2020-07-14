'''
    123. 买卖股票的最佳时机
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            对暴力法的优化
        """
        # 边界，prices为空
        if not prices:
            return 0

        def buyOnce(r):
            """
                只买卖一次的函数

                Args:
                    r: 从第几天开始（从1开始算）

                Returens:
                    buyDay: 股票从哪一天买进
                    a2: 最大利润
            """
            a2 = 0
            buyDay = -1
            if r+1<len(prices):
                minStock2 = prices[r+1]
                # 当前股票最小值所对应的时间
                last = r+1
                for i in range(r+2,len(prices)):
                    if prices[i] - minStock2>a2:
                        # 成功买卖后，更新最大利润和买进时间
                        a2 = prices[i]-minStock2
                        buyDay = last
                    if minStock2>=prices[i]:
                        # 当有股票比当前最小值还小时，更新最小值和此股票对应的时间
                        minStock2 = prices[i]
                        last = i
            else:
                return None,None
            return buyDay,a2

        r = 1
        a1 = 0
        minStock1 = prices[0]
        # 只买卖一次
        _,ans = buyOnce(-1)
        # 如果只买卖一次利润为0，则说明买卖两次利润也为0
        if ans==0:
            return 0

        # 如果只买卖一次的买进时间大于剩下的开始时间
        # 则说明，剩下的这段时间不需要重新再跑一遍buyOnce函数
        if _>r:
            index,a2 = _,ans
        # 否则，获得剩下时间的最大理论和买进时间
        else:
            index,a2 = buyOnce(r)

        # 开始遍历，拆分时间为两段[0,r],[r+1,len(prices)]
        # 对于[0,r]而言，这段的最大利润关于r为（不严格）单调递增
        # 对于[r+1,len(prices)]而言，这段的最大利润关于r（不严格）单调递减
        while r+1 < len(prices):
            # 如果[0,r]段随着r的变大而变大，则需要更新[r+1,len(prices)]段
            if prices[r]-minStock1>a1:
                # 更新[0,r]的最大利润
                a1 = prices[r]-minStock1
                # 更新[r+1,len(prices)]段的利润
                if index < r:
                    # 如果上次买入时间比r小，则需要更新
                    index,a2 = buyOnce(r)
                # 更新最终利润
                ans = max(ans,a1+a2)
            # else:
                # 如果[0,r]的理论没有变大，后面也不需要更新（因为一定会变小）
            # 更新[0,r]段的最小股票时间
            minStock1 = min(minStock1,prices[r])
            r += 1
        return ans

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            分段+dp
        """
        if not prices:
            return 0

        f = [0]*len(prices)
        g = [0]*len(prices)

        # 顺序
        minStock = prices[0]
        for i in range(1,len(prices)):
            f[i] = max(f[i-1],prices[i]-minStock)
            minStock = min(minStock,prices[i])
        
        # 逆序
        maxStock = prices[-1]
        for i in range(len(prices)-2,-1,-1):
            g[i] = max(g[i+1],maxStock - prices[i])
            maxStock = max(maxStock,prices[i])

        ans = 0
        for i in range(len(prices)):
            ans = max(ans,f[i]+g[i])
        return ans
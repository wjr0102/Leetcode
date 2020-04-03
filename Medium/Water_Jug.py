'''
    使用list作为flag的类型，in操作过慢，会导致无法通过
'''
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z==0:
            return True
        if (x+y<z):
            return False
        
        queue = [(0,0)]
        flags = set()
        flags.add((0,0))
        while queue:
            # print(queue)
            cur = queue.pop()
            remain_x = cur[0]
            remain_y = cur[1]

            if (remain_x==z) or (remain_y==z) or (remain_x+remain_y==z):
                return True

            # Fill x
            if (x,remain_y) not in flags:
                flags.add((x,remain_y))
                queue.append((x,remain_y))
            
            # Fill y
            if (remain_x,y) not in flags:
                flags.add((remain_x,y))
                queue.append((remain_x,y))


            # Empty x
            if (0,remain_y) not in flags:
                flags.add((0,remain_y))
                queue.append((0,remain_y))


            # Empty y
            if (remain_x,0) not in flags:
                flags.add((remain_x,0))
                queue.append((remain_x,0))


            # Pour x to y
            next_x = remain_x - min(remain_x,y-remain_y)
            next_y = remain_y + min(remain_x,y-remain_y)
            if (next_x,next_y) not in flags:
                flags.add((next_x,next_y))
                queue.append((next_x,next_y))

            
            # Pour y to x
            next_x = remain_x + min(remain_y,x-remain_x)
            next_y = remain_y - min(remain_y,x-remain_x)
            if (next_x,remain_y) not in flags:
                flags.add((next_x,next_y))
                queue.append((next_x,next_y))

        return False

'''
    数学角度：

    每次操作对水的总量有且仅有可能以下四种影响：
        - 增加x
        - 增加y
        - 减少x
        - 减少y
    因为
        - 对不满的水桶加水=加满此水桶
        - 倒掉不满的水桶里的水=清空此水桶

    因此只需令以下公式有解（z<=x+y）：
        ax + by = z

    由贝祖定理知: 当且仅当z是x,y的最大公约数的倍数，有解
'''
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x+y<z:
            return False
        if z == 0:
            return True

        return z % gcd(x,y)==0
        
    def gcd(x,y):
        a = x % y
        if a==0:
            return x
        else:
            return gcd(y,a)
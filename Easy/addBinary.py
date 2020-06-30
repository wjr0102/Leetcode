'''
    67. 二进制求和

    tips: list转string要求元素都为字符串
'''
class Solution:
    '''
        高精度加法——二进制版
    '''
    def addBinary(self, a: str, b: str) -> str:
        la = len(a)
        lb = len(b)

        def add(s1,s2):
            """
                要求s1的长度小于等于s2时的二进制高精度加法

                Args:
                    s1: 较短的字符串
                    s2: 较长的字符串

                Returns:
                    res: 字符串形式的答案
            """
            res = [0]*(len(s2)+1)
            c = 0
            for i in range(-1,-len(s1)-1,-1):
                s = int(s1[i]) + int(s2[i]) + c
                c = s//2
                res[i] = str(s % 2)

            for i in range(-len(s1)-1,-len(s2)-1,-1):
                s = int(s2[i]) + c
                c = s//2
                res[i] = str(s % 2)
            
            if c==0:
                res = res[1:]
            else:
                res[0] = '1'

            return "".join(res)

        if la<=lb:
            return add(a,b)
        else:
            return add(b,a)

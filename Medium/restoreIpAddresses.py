'''
    93. 复原ip地址
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 长度判断
        if len(s)>12 or len(s)<4:
            return []
        # 储存结果
        res = []

        # 递归函数
        def get(ss,pos,ans):
            """
                @Args:
                    ss: 当前剩下的字符串
                    pos: ip地址的位置，从1开始
                    ans: 当前的ip地址
            """
            # print(ss,pos,ans)
            # 如果当前剩下的字符串为空，则返回
            if not ss:
                return False
            # 当处理到最后一个ip地址位置时
            if pos==4:
                # 判断最后的字符串是否合法
                if ss[0]=='0' and len(ss)>1:
                    return False
                if int(ss)>255:
                    return False
                # 合法则加入res
                else:
                    res.append(ans+ss)
                    return True
            # 处理其他位置时
            # 判断是否以0开头，若是则0为单独一位
            if ss[0]=='0':
                get(ss[1:],pos+1,ans+'0.')
            # 否则循环3位
            else:
                for i in range(1,min(4,len(ss))):
                    if (int(ss[:i]))>255:
                        continue
                    get(ss[i:],pos+1,ans+ss[:i]+'.')

        get(s,1,'')

        return res
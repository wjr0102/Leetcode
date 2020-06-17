class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        NUMS = {"0","1","2","3","4","5","6","7","8","9"}
        ans = ""

        for c in s:
            if c == "]":
                # 出栈
                res = ""
                while stack:
                    a = stack.pop()
                    if a == "[":
                        break
                    else:
                        res += a
                count = ""
                while stack:
                    a = stack.pop()
                    if a in NUMS:
                        count += a
                    else:
                        stack.append(a)
                        break
                count = count[::-1]
                res = res*(int)(count)
                if not stack:
                    ans += res[::-1]
                    res = ""
                else:
                    stack.append(res)
            else:
                # 入栈
                stack.append(c)

        res = ""
        while stack:
            res += stack.pop()
        ans += res[::-1]
        return ans
class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return S
        ans = ""
        count = 1
        last = S[0]
        for i in range(1,len(S)):
            if S[i]==last:
                count += 1
            else:
                ans += last + str(count)
                last = S[i]
                count = 1
        ans += last + str(count)
        if len(ans)<len(S):
            return ans
        else:
            return S
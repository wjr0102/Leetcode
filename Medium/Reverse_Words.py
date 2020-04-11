class Solution:
    def reverseWords(self, s: str) -> str:
        # Remove Whitespace
        s = s.strip()
        words = []
        word = ""
        for c in s:
            if c==" " and word!="":
                words.append(word)
                word = ""
            elif c!=" ":
                word += c
        words.append(word)
        ans = ""
        for word in words[::-1]:
            ans += word + " "
        return str(ans[:-1])

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split(" ")
        ans = ""
        for i in range(len(words)-1,-1,-1):
            if words[i]:
                ans += words[i] + " "
        return ans[:-1]

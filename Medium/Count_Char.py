class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for word in words:
            is_learn = True
            for c in word:
                if word.count(c) > chars.count(c):
                    is_learn = False
                    break
            if is_learn:
                ans += len(word)

        return ans
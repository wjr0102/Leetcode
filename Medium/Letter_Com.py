class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        ans = ['']
        for num in digits:
            ans = [pre+suf for pre in ans for suf in dic[num]]
        return ans
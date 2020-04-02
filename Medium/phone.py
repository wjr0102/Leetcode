class Solution:
    dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6':
           'mno', '7': 'pqrs', '8': 'tuv', 9: 'wxyz'}
    result = []

    def letterCombinations(self, digits: str) -> List[str]:
        card = 0
        factor = 1
        for num in digits:
            if num == '7' or num == '9':
                factor *= 4
            else:
                factor *= 3
            card += factor
        result = ["" for i in range(factor)]
        for num in digits:
            pass

    def rank(self, digits: str, step: int):
        if step + 1 == len(digits):
            return

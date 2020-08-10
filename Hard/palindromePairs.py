'''
    336. 回文对
'''
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        dic = {}
        for i in range(len(words)):
            word = words[i]
            dic[word] = i

        res = []
        flags = set()

        def check(s):
            p0 = 0
            p1 = len(s)-1
            while p0<p1 and s[p0]==s[p1]:
                p0 +=1
                p1 -=1
            if p0>=p1:
                return True
            return False

        # word作为后缀
        for word in words:
            if word=="":
                continue
            # 判别当前单词的回文性
            pa = [0] # 空字符串肯定是回文
            for i in range(len(word)):
                if check(word[:i+1]):
                    pa.append(i+1)
            for i in pa:
                wr = word[i:][::-1]
                if wr!=word and wr in dic:
                    res.append([dic[wr],dic[word]])
                    flags.add((dic[wr],dic[word]))

        # word作为前缀
        for word in words:
            if word=="":
                continue
            ori = word
            word = word[::-1]
            # 判别当前单词的回文性
            pa = [0] # 空字符串肯定是回文
            for i in range(len(word)):
                if check(word[:i+1]):
                    pa.append(i+1)
            for i in pa:
                wr = word[i:]
                # print(ori,index,wr)
                if wr!=ori and wr in dic and (dic[ori],dic[wr]) not in flags:
                    res.append([dic[ori],dic[wr]])
            
        
        return res


                
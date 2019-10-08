class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dic = {}
        for i in chars:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        num = 0
        for word in words:
            dic1 = dic.copy()
            count = 0
            for alpha in word:
                if alpha in dic1:
                    count += 1
                    dic1[alpha] -= 1
                    if dic1[alpha] == 0:
                        del dic1[alpha]
                else:
                    break
                    
                if count == len(word):
                    num += count
                
        return num

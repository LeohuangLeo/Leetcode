#13
class Solution:
    def romanToInt(self, s: str) -> int:
        s = s[::-1]
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        F = None
        Sum = 0
        for i in range(len(s)):
            if F and dic[s[i]] < F:
                Sum -= 2*dic[s[i]]
            Sum += dic[s[i]]
            F = dic[s[i]]
        return Sum

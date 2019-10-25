class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left, right = 0, 0
        ttl = 0
        num = set()
        while left < len(s) and right < len(s):
            if s[right] in num:
                if s[left] in num:
                    num.remove(s[left])
                left += 1
            else:
                num.add(s[right])
                right += 1
                ttl = max(ttl, len(num))
        return ttl
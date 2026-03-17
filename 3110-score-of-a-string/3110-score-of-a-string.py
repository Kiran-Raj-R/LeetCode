class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        l = len(s)
        for i in range(l-1):
            res += abs(ord(s[i])-ord(s[i+1]))
        return res
class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        c, c1, prev = 0, 0, '0'
        for ch in s:
            c1 += ch == '1'
            c += (-(ch == '0' and prev == '1')) & c1
            prev = ch
        return c
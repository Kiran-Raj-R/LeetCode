class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        res = ""
        temp = [0] * n
        for i in range(n):
            temp[indices[i]] = s[i]
        for char in temp:
            res += char
        return res
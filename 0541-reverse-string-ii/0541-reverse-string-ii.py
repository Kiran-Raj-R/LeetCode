class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]
        else:
            blocks = [s[i:i+k] for i in range(0,len(s),k)]
            for block in range(0,len(blocks),2):
                blocks[block] = blocks[block][::-1]
            res = ''.join(blocks)
        return res                
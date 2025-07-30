class Solution:
    def sortVowels(self, s: str) -> str:
        vow = []
        pos = []
        for i,ch in enumerate(s):
            if ch.lower() in {'a','e','i','o','u'}:
                vow.append(ch)
                pos.append(i)
        res = list(s)
        vow.sort()
        for i,c in zip(pos,vow):
            res[i] = c
        return ''.join(res)
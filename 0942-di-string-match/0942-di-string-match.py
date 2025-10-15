class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        l,r = 0,len(s)
        for n in s:
            if n == 'I':
                res.append(l)
                l += 1
            else:
                res.append(r)
                r -= 1
        res.append(l)
        return res         
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        tally, res = 1, 0
        tri = lambda x: x * (x+1) // 2
        for l, r in pairwise(prices):
            if r == l - 1:
                tally += 1
            else:
                res += tri(tally)
                tally = 1
        res += tri(tally)
        return res
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        n = len(piles)
        for i in range(n // 3, n, 2): #n//3 - 1 will be the piles bob will pick
            res += piles[i]
        return res
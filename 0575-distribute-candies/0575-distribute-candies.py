class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy = {}
        n = len(candyType)
        for c in candyType:
            if c in candy:
                candy[c] += 1
            else:
                candy[c] = 1

        if len(candy) > n/2:
            return n // 2
        return len(candy)
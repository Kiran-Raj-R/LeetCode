class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy = {}
        n = len(candyType)
        for i in range(n):
            if candyType[i] in candy:
                candy[candyType[i]] += 1
            else:
                candy[candyType[i]] = 1
        # for c in candyType:
        #     if c in candy:
        #         candy[c] += 1
        #     else:
        #         candy[c] = 1

        if len(candy) > n/2:
            return n // 2
        else:
            return len(candy)
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        # ans = j = 0
        # for i, x in enumerate(forts):
        #     if x:
        #         if forts[j] == -x:
        #             ans = max(ans, i-j-1)
        #         j = i
        # return ans

        l, count = 0, 0
        for r in range(len(forts)):
            if forts[r] != 0:
                if forts[l] == 1 and forts[r] == -1 or forts[l] == -1 and forts[r] == 1:
                    count = max(count, r - l - 1)
                l = r
        return count
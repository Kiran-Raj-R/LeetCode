class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ans = j = 0
        for i, x in enumerate(forts):
            if x:
                if forts[j] == -x:
                    ans = max(ans, i-j-1)
                j = i
        return ans
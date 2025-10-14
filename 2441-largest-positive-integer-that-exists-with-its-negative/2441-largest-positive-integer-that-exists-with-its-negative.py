class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        m = 0
        for n in nums:
            if -(n) in nums and n > m:
                m = n
        if m:
            return m
        return -1
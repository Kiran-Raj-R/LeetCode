class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = float('inf')
        for num in nums:
            d_sum = 0
            while num > 0:
                d_sum += num % 10
                num //= 10
            res = min(res, d_sum)
        return res
            
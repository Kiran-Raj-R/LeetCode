class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        lsum, res = 0, 0
        for i in range(len(nums)-1):
            lsum += nums[i]
            rsum = total - lsum
            if (lsum%2) == (rsum%2):
                res += 1
        return res
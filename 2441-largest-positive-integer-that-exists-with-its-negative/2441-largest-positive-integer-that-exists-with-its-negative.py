class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = -1
        nums.sort()
        while l < r:
            if nums[l] + nums[r] == 0:
                res = max(res, nums[r])
                l += 1
                r -= 1
            elif nums[l] + nums[r] < 0:
                l += 1
            else:
                r -= 1
        return res
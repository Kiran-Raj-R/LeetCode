class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avgs = []
        nums.sort()
        l,r = 0,len(nums) - 1
        while l < r:
            a = (nums[l] + nums[r]) / 2
            avgs.append(a)
            l += 1
            r -= 1
        return min(avgs)
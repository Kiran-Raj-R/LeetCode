class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        diff = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    diff.append(nums[j] - nums[i])
        if diff:
            return max(diff)
        return -1
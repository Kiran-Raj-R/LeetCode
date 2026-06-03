class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        ind = nums.index(largest)
        for num in nums:
            if num != largest and largest < 2*num:
                return -1
        return ind
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        for i in range(len(nums)):
            res = nums[i]
            if res == target:
                return i
            elif res < target and target < nums[i+1]:
                return i+1
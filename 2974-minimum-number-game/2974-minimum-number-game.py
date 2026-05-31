class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        l = len(nums)
        nums.sort()
        for i in range(0,l-1,2):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # index = 0
        # for i in range(len(nums)):
        #     if nums[i] % 2 == 0:
        #         nums[index],nums[i] = nums[i], nums[index]
        #         index += 1
        # return nums
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] % 2 > nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] % 2 == 0:
                left += 1
            if nums[right] % 2 == 1:
                right -= 1
        return nums
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # first,second,third = float(-inf),float(-inf),float(-inf)
        # for num in nums:
        #     if num > first:
        #         first,second,third = num,first,second
        #     elif first > num > second:
        #         second,third = num,second
        #     elif second > num > third:
        #         third = num
        # if third != float(-inf):
        #     return third
        # else:
        #     return first
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)
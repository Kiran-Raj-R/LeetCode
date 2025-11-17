class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res, c = [], 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    c += 1
            res.append(c)
            c = 0
        return res
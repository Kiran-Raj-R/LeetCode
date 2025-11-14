class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, c = 0, 0
        for num in nums:
            if num == 1:
                c += 1
            else:
                res = max(res,c)
                c = 0
        return max(res,c)
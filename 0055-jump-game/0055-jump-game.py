class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = 0
        for num in nums:
            if l < 0:
                return False
            elif num > l:
                l = num
            l -= 1
        return True
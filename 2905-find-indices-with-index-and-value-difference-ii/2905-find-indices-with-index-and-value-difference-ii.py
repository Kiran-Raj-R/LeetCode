class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        s,l = 0,0
        for i in range(indexDifference,len(nums)):
            if nums[i-indexDifference] < nums[s]:
                s = i - indexDifference
            if nums[i-indexDifference] > nums[l]:
                l = i - indexDifference
            if nums[i] - nums[s] >= valueDifference:
                return [s,i]
            if nums[l] - nums[i] >= valueDifference:
                return [l,i]
        return [-1,-1]
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = {}
        res = []
        for num in nums:
            if num in seen:
                res.append(num)
            seen[num] = num
        return res
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = {}
        for num in nums:
                res[num] = res.get(num,0) + 1
        return [k for k,v in res.items() if v > n//3]
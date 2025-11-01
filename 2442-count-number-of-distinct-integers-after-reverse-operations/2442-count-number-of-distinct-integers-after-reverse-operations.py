class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        # res = set(nums)
        # for num in nums:
        #     res.add(int(str(num)[::-1]))
        # return len(res)
        return len(set(nums) | {int(str(x)[::-1]) for x in nums})
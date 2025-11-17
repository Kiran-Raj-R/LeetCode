class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # res = []
        # for i in nums:
        #     c = 0
        #     for j in nums:
        #         if j < i:
        #             c += 1
        #     res.append(c)
        # return res
        sorted_nums = sorted(nums)
        r = {}
        for i,v in enumerate(sorted_nums):
            if v not in r:
                r[v] = i
        return [r[x] for x in nums]
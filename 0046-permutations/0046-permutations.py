class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def fun(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for num in nums:
                if num in curr:
                    continue

                curr.append(num)
                fun(curr)
                curr.pop()
        fun([])
        return res
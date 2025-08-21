class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # res = 0
        # for num in nums:
        #     res = res ^ num
        # return res
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for k,v in freq.items():
            if v == 1:
                return k
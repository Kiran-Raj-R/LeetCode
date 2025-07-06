class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        n = len(nums)
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for k,v in freq.items():
            if v > n // 2:
                return k
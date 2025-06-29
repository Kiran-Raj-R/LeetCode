class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        maxim = -1
        for n in nums:
            val = freq.get(n,0)
            freq[n] = val + 1
            if maxim < (val + 1):
                maxim = val +1
        count = 0
        for _,v in freq.items():
            if v == maxim:
                count += 1
        return count * maxim
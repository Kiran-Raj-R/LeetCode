class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
                res.append(num)
            else:
                freq[num] = 1
        return res
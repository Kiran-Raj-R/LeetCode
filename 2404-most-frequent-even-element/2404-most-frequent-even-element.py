class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = {}
        val,m = 10**6,0
        for num in nums:
            if num % 2 == 0:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1
                if freq[num] > m or freq[num] == m and num < val:
                    val,m = num,freq[num]
        return -1 if m == 0 else val
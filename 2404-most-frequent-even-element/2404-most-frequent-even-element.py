class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_freq = {}
        max_num, max_freq = 10**6, 0
        for num in nums:
            if num % 2 == 0:
                if num in even_freq:
                    even_freq[num] += 1
                else:
                    even_freq[num] = 1
                if even_freq[num] > max_freq or even_freq[num] == max_freq and num < max_num:
                    max_num, max_freq = num, even_freq[num]
        return -1 if max_freq == 0 else max_num
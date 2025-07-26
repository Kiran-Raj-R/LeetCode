class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for k,v in freq.items():
            if v == 1:
                pass
            elif v == 2:
                return True
            else:
                for j in range(2,v):
                    if v % j == 0:
                        break
                else:
                    return True
        return False
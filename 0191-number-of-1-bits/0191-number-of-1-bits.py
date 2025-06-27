class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        count = 0
        for b in binary:
            if b == "1":
                count += 1
        return count
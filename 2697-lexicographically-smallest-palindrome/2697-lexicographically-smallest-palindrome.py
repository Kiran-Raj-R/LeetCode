class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l, r = 0, len(s) - 1
        ls = [ch for ch in s]
        while l < r:
            if ls[l] > ls[r]:
                ls[l] = ls[r]
            elif ls[r] > ls[l]:
                ls[r] = ls[l]
            l += 1
            r -= 1
        return ''.join(ls)
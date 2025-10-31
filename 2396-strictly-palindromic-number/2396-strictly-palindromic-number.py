class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # for i in range(2, n-1):
        #     t = n
        #     res = ""
        #     while t > 0:
        #         rem = t % i
        #         res += str(rem)
        #         t = t // i
        #     if res != res[::-1]:
        #         return False
        # return True
        return not (n >= 4)
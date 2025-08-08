class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return False

        # num = x
        # pal = 0

        # while x > 0:
        #     rem = x % 10
        #     pal = pal * 10 + rem
        #     x = x // 10
        # return pal == num

        # s = str(x)
        # rev = s[::-1]
        # return rev == s

        num = str(x)
        l,r = 0, len(num) - 1
        while l < r:
            if num[l] == num[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
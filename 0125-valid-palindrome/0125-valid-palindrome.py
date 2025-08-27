class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join([ch for ch in s.lower() if ch.isalnum()])
        return res == res[::-1]
class Solution:
    def reverseWords(self, s: str) -> str:
        # return ' '.join(s.split()[::-1])
        words = [i for i in s.split()]
        left, right = 0, len(words) - 1
        while left < right:
            words[left],words[right] = words[right],words[left]
            left += 1
            right -= 1
        return ' '.join(words)
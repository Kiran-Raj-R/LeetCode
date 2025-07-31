class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s_ls = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if s_ls[left] in vowels and s_ls[right] in vowels:
                s_ls[left], s_ls[right] = s_ls[right], s_ls[left]
                left += 1
                right -= 1
            elif s_ls[left] not in vowels:
                left += 1
            elif s_ls[right] not in vowels:
                right -= 1
        return ''.join(s_ls)
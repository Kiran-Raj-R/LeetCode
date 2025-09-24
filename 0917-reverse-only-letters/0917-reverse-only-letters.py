class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alph = ''.join([l for l in s if l.isalpha()])
        rev = []
        left, right = 0, -1
        for i in range(len(s)):
            if s[i].isalpha():
                rev.append(alph[right])
                right -= 1
                left += 1
            else:
                rev.append(s[left])
                left += 1
        return ''.join(rev)
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        flag = 0
        if word == word.upper() or word == word.lower() or (word[0].isupper() and word[1:].islower()):
            flag = 1
        return flag == 1
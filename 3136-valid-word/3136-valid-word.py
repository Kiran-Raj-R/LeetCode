class Solution:
    def isValid(self, word: str) -> bool:
        vowels = "aeiouAEIOU"
        if len(word) < 3:
            return False
        vowel = 0
        consonant = 0
        for w in word:
            if not w.isalnum():
                return False
            if w.isalpha():
                if w in vowels:
                    vowel += 1
                else:
                    consonant += 1
        return vowel > 0 and consonant > 0
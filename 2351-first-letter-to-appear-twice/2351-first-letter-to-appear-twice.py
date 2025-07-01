class Solution:
    def repeatedCharacter(self, s: str) -> str:
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
                if freq[char] == 2:
                    return char
            else:
                freq[char] = 1
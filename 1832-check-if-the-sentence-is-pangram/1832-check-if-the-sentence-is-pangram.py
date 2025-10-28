class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = {}
        for char in sentence:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
        return len(seen) == 26
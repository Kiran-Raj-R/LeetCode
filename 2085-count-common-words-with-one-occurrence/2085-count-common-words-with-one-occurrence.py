class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        freq1 = {}
        freq2 = {}
        for word in words1:
            if word not in freq1:
                freq1[word] = 1
            else:
                freq1[word] += 1
        for word in words2:
            if word not in freq2:
                freq2[word] = 1
            else:
                freq2[word] += 1
        
        res = 0
        for word in words1:
            if word in words2 and freq1[word] == 1 and freq2[word] == 1:
                res += 1
        
        return res
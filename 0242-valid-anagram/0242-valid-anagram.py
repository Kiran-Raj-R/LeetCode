class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1,freq2 = {},{}
        for ch in s:
            if ch in freq1:
                freq1[ch] += 1
            else:
                freq1[ch] = 1
        
        for c in t:
            if c in freq2:
                freq2[c] += 1
            else:
                freq2[c] = 1
        
        if len(s) == len(t) and freq1 == freq2:
            return True
        else:
            return False
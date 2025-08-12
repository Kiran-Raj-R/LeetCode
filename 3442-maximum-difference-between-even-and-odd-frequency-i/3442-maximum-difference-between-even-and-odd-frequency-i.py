class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        odd , even = [], []
        diff = []
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        for k,v in freq.items():
            if v % 2 == 0:
                even.append(v)
            else:
                odd.append(v)
        for o in odd:
            for e in even:
                diff.append(o-e)
        
        return max(diff)
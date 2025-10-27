class Solution:
    def frequencySort(self, s: str) -> str:
        res = ""
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        freq2 = sorted(freq.items(),key=lambda x:x[1],reverse=True)
        for k,v in freq2:
            res += (k*v)
        return res
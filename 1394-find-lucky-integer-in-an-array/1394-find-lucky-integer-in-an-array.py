class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for a in arr:
            if a in freq:
                freq[a] += 1
            else:
                freq[a] = 1
        lucky = [k for k,v in freq.items() if k == v]
        if lucky:
            return max(lucky)
        return -1
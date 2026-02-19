class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dict1 = {}
        for ch in arr:
            if ch in dict1:
                dict1[ch] += 1
            else:
                dict1[ch] = 1
        lis = [ke for ke,v in dict1.items() if v == 1]
        return lis[k-1] if len(lis) >= k else ""
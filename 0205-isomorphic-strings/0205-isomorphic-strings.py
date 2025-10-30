class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash1, hash2 = {}, {}
        for i,j in zip(s,t):
            if i in hash1:
                if hash1[i] != j:
                    return False
            else:
                hash1[i] = j
            if j in hash2:
                if hash2[j] != i:
                    return False
            else:
                hash2[j] = i
        return True
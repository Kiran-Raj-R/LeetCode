class Solution:
    def isPathCrossing(self, path: str) -> bool:
        i,j = 0,0
        s = set()
        s.add((i,j))
        for p in path:
            if p == 'N':
                i += 1
            elif p == 'S':
                i -= 1
            elif p == 'E':
                j += 1
            elif p == 'W':
                j -= 1
                
            if (i,j) in s:
                return True
            s.add((i,j))
        return False
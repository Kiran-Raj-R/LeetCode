class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        i = j = k = 0
        for _ in range(n-1):
            m = min(res[i]*2,res[j]*3,res[k]*5)
            res.append(m)
            if m == res[i]*2:
                i += 1
            if m == res[j]*3:
                j += 1
            if m == res[k]*5:
                k += 1
        return res[-1]
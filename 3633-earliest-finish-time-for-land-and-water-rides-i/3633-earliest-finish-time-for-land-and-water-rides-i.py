class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res = float('inf')
        n, m = len(landStartTime), len(waterStartTime)
        for i in range(n):
            a, b = landStartTime[i], landDuration[i]
            for j in range(m):
                c, d = waterStartTime[j], waterDuration[j]

                landEnd = a + b
                startWater = max(landEnd, c)
                finish1 = startWater + d

                waterEnd = c + d
                startLand = max(waterEnd, a)
                finish2 = startLand + b

                res = min(res, finish1, finish2)
        return res
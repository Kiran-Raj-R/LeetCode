class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res, pre = 0, 0
        for i in range(1, len(colors)):
            if colors[i] == colors[pre]:
                res += min(neededTime[i],neededTime[pre])
                if neededTime[i] > neededTime[pre]:
                    pre = i
            else:
                pre = i
        return res
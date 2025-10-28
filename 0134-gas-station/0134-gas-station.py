class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        fueltank, start = 0, 0
        for i in range(len(gas)):
            fueltank += (gas[i] - cost[i])
            if fueltank < 0:
                start = i + 1
                fueltank = 0
        return start
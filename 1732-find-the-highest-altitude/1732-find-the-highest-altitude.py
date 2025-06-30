class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        altitudes.append(gain[0])
        for i in range(1,len(gain)):
            altitudes.append(gain[i] + altitudes[i])
        return max(altitudes)
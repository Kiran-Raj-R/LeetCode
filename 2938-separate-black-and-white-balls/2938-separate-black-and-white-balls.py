class Solution:
    def minimumSteps(self, s: str) -> int:
        black, swap = 0, 0
        for ball in s:
            if ball == '0':
                swap += black
            else:
                black += 1
        return swap
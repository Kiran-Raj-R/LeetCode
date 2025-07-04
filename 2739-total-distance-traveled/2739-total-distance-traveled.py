class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        res = 0
        while mainTank >= 5 and additionalTank >= 1:
            res += 10 * 5
            mainTank -= 4
            additionalTank -= 1
        return res + (mainTank * 10)
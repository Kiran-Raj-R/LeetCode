class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        res = []
        i = 0
        while n:
            num = n % 10
            if num:
                res.append(num*10**i)
            i += 1
            n //= 10
        return res[::-1]
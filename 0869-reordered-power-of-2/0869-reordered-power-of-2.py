class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def digit_count(num):
            c = [0] * 10
            if num == 0:
                c[0] = 1
                return tuple(c)
            while num > 0:
                c[num % 10] += 1
                num //= 10
            return tuple(c)
        num_count = digit_count(n)
        for i in range(30):
            power = 1 << i
            if digit_count(power) == num_count:
                return True
        return False
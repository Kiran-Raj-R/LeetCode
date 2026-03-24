class Solution:
    def maximum69Number (self, num: int) -> int:
        tens = (1000, 100, 10, 1)
        for ten in tens:
            r = num // ten % 10
            if r == 6:
                return num + 3 * ten
        return num
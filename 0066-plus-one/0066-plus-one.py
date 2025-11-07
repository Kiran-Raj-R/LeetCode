class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # res = 0
        # for digit in digits:
        #     res = (res * 10) + digit
        # return [int(d) for d in str(res+1)]
        return [int(d) for d in str(int(''.join(map(str,digits)))+1)]
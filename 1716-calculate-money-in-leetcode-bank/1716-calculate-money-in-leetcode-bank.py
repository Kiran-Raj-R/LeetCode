class Solution:
    def totalMoney(self, n: int) -> int:
        # q, r = divmod(n,7)
        # return 28*q+7*q*(q-1)//2 + (2*q+r+1)*r//2
        mon = 0
        c , res = 0,0
        for i in range(1,n+1):
            if c == 7:
                mon = i // 7 + 1
                c = 0
            else:
                mon += 1
            res += mon
            c += 1
        return res
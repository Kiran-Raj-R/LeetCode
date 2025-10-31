class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # res,pos,neg = [],[],[]
        # for num in nums:
        #     if num > 0:
        #         pos.append(num)
        #     else:
        #         neg.append(num)
        # for i in range(len(pos)):
        #     res.append(pos[i])
        #     res.append(neg[i])
        # return res
        res = [0] * len(nums)
        p, n = 0, 1
        for num in nums:
            if num > 0:
                res[p] = num
                p += 2
            else:
                res[n] = num
                n += 2
        return res
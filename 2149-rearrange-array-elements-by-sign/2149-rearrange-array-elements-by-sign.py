class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res,pos,neg = [],[],[]
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        l, r = 0, 0
        while l < len(pos) and r < len(neg):
            res.append(pos[l])
            l += 1
            res.append(neg[r])
            r += 1
        return res
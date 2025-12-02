class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # res = {}
        # for num in nums:
        #         res[num] = res.get(num,0) + 1
        # return [k for k,v in res.items() if v > n//3]
        c1 = c2 = 0
        cand1 = cand2 = None
        for num in nums:
            if num == cand1:
                c1 += 1
            elif num == cand2:
                c2 += 1
            elif c1 == 0:
                cand1 = num
                c1 = 1
            elif c2 == 0:
                cand2 = num
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        
        res = []
        if nums.count(cand1) > len(nums) // 3:
            res.append(cand1)
        if cand2 is not None and nums.count(cand2) > len(nums) // 3:
            res.append(cand2)
        return res
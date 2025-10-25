class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        m = {}
        for n in nums2:
            while res and n > res[-1]:
                m[res.pop()] = n
            res.append(n)
        for n in res:
            m[n] = -1
        return [m[i] for i in nums1] 
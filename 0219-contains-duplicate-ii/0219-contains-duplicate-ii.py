class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ind = {}
        for i,j in enumerate(nums):
            if j in ind and abs(i-ind[j] <= k):
                return True
            else:
                ind[j] = i
        return False
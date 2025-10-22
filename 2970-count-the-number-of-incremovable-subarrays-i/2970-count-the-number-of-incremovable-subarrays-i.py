class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        if n == 0:
            return 0
        l,r = 0,n-1
        while(l+1 < n and nums[l+1] > nums[l]):
            l += 1
        if l == n-1:
            return (n*(n+1)) // 2
        while(r>0 and nums[r] > nums[r-1]):
            r -= 1

        res += l+1
        res += n - r+1

        i,j = 0,r
        while(i <= l):
            while(j < n and nums[i] >= nums[j]):
                j += 1
            res += n-j
            i += 1
        return res
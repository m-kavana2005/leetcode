class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        g=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]+i >= g:
                g=i
        return g==0
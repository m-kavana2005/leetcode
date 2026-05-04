class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps,curend,farthest=0,0,0
        for i in range(len(nums)-1):
            farthest = max(farthest,i+nums[i])
            if i==curend:
                jumps+=1
                curend=farthest
        return jumps
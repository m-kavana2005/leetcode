class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0   # farthest index we can reach
    
        for i in range(len(nums)):
            if i > max_reach:
                return False   # we cannot even reach this index
        
            max_reach = max(max_reach, i + nums[i])
    
        return True   # we can reach the last index
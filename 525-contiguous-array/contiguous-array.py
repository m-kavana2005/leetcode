class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = 0
        max_len = 0
        first_seen = {0:-1}
        for i in range(len(nums)):
            if nums[i]==0:
                prefix_sum-=1
            else:
                prefix_sum+=1
            if prefix_sum in first_seen:
                p_len = i-first_seen[prefix_sum]
                max_len=max(max_len,p_len)
            else:
                first_seen[prefix_sum]=i
        return max_len
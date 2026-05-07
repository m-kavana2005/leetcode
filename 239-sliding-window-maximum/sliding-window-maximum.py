class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq=deque()
        res=[]
        for i in range(len(nums)):
            if dq and dq[0] < i-k+1:
                dq.popleft()
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i>=k-1:
                res.append(nums[dq[0]])
        return res
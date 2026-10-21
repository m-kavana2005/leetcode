class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n=len(nums)
        w_sum = sum(nums[:k])
        max_sum = w_sum
        max_start_index = 0
        for i in range(n-k):
            w_sum = w_sum - nums[i] + nums[i+k]
            if w_sum > max_sum:
                max_sum = w_sum
                max_start_index = i+1
        return max_sum/k
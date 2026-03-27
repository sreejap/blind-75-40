class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        curr_sub = nums[0]

        for i in range (1,len(nums)):
            curr_sub = max(nums[i], curr_sub+nums[i])
            max_sub = max (curr_sub, max_sub)
        
        return max_sub

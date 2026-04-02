# https://leetcode.com/problems/partition-equal-subset-sum/
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # create a 2d array
        sum_num = 0
        for n in nums:
            sum_num += n
        
        if sum_num %2 !=0:
            return False

        target = sum_num // 2 # we only want the half because we are partitioning into 2 subsets

        n = len(nums)
        dp = [[False] * (target+1) for _ in range (n+1) ]

        dp [0][0] = True

        for i in range (1,n+1):            
            dp [i][0] = True # sum 0 is always possible

        for i in range (1,n+1):
            curr = nums[i-1]            
            for j in range (1,target+1):
                # key idea- at each step i, I consider the element nums[i-1] and decide whether to include it or not to make the sum j
                # dp[i][j] represents whether I can form sum j using the first i elements.
                # At each step, I look at nums[i-1] and decide whether to include it or not—if I exclude it, I carry forward the previous result; if I include it, I check whether I could form j - nums[i-1] before.
                if j < curr:
                    dp [i][j] = dp[i-1][j] # if j is less than current elemnt, we don't include curr element and we grab answer from prev row
                
                else:
                    dp [i][j] = dp[i-1][j] or dp[i-1][j-curr]
        return dp [n][target]

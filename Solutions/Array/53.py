class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = nums[0] 
        currentSum = nums[0]  
        n = len(nums)
        
        for i in range(1, n): 
            currentSum = max(nums[i], currentSum + nums[i])  
            maxSum = max(maxSum, currentSum)  
        
        return maxSum

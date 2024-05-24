import sys

class Solution:
    def maxSubArray(self, nums: [-2,1,-3,4,-1,2,1,-5,4]) -> int:
        n=len(nums)
        maxSum=-sys.maxsize
        for i in range(n):
            sum=0
            for j in range(i,n):
                sum +=nums[j]
                maxSum=max(maxSum,sum)

        return maxSum

n1=[-2,1,-3,4,-1,2,1,-5,4]
print(Solution())
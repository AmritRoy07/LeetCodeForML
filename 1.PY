class Solution:
    def twoSums(self, nums:list[int],target:int)->list[int]:
        m={}
        for i, x in enumerate(nums):
            y=target-x
            if y in m:
                return [m[y],i]
            m[x]=i

nums_list = [2, 7, 11, 15]
target_sum = 11

result_indices = Solution().twoSums(nums_list, target_sum)

print(result_indices) 

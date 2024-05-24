class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        output=nums[0]+nums[1]+nums[2]
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            n=i+1
            r=len(nums) -1
            while n<r:
                add=nums[0]+nums[1]+nums[2]
                if add==target:
                    return add
                elif add< target:
                    n+=1
                else:
                    r-=1        

            return output
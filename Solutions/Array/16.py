class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')  
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(target - total) < abs(target - closest_sum):
                    closest_sum = total
                if total == target:
                    return total
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return closest_sum

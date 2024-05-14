class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()  # Sort the list to make the solution unique and avoid duplicates
        n = len(nums)

        for i in range(n - 2):  # Loop until the third-to-last element
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicate elements for left and right pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result

num = [-1, 0, 1, 2, -1, 4]
solution = Solution()
result = solution.threeSum(num)
print(result)

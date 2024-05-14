class Solution:
    def maxArea(self, height: list[int]) -> int:
        i=0
        j=len(height)-1
        out=0
        while i < j:
            current_area = min(height[i], height[j]) * (j-i)
            out = max(out, current_area)  
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1    
        return out       

h=[1,8,6,2,5,4,8,3,7]
sol=Solution().maxArea(h)
print(sol)

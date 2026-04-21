class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1

        area = 0
        best = 0
        while left < right:
            area = (right - left) * min(heights[right], heights[left])
            if area > best:
                best = area
            if min(heights[right], heights[left]) == heights[right]:
                right -= 1
            else:
                left += 1
        
        return best
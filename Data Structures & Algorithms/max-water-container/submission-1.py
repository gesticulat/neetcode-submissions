class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        l, r = 0, len(heights) - 1

        while l < r:
            length = r - l
            height = min(heights[l], heights[r])
            m = max(m, length * height)
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return m
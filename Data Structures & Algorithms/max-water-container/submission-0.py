class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest_area = 0
        p1, p2 = 0, len(heights) - 1

        while p1 != p2:
            length = p2 - p1
            height = min(heights[p1], heights[p2])
            area = length * height
            if area > largest_area:
                largest_area = area
            
            if heights[p1] > heights[p2]:
                p2 -= 1
            else:
                p1 += 1
        return largest_area
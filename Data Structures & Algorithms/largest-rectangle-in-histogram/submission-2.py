class Solution:
    def addItem(self, stack: List[int], new_item: int) -> List[int]:
        while stack and stack[-1] < new_item:
            stack.pop()
        stack.append(new_item)
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        tallest = max(heights)
        stack = [tallest]
        span = 0
        for y in range(1, tallest+1):
            for bar in heights:
                if bar >= y:
                    span += 1
                else:
                    self.addItem(stack, y*span)
                    span = 0
            self.addItem(stack, y*span)
            span = 0
        return stack[0]
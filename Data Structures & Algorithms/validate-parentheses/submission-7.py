class Solution:
    def isValid(self, s: str) -> bool:
        table = str.maketrans(")]}", "([{")
        stack = []

        for char in s:
            if char in "([{":
                stack.append(char)
            elif stack and stack[-1] == char.translate(table):
                stack.pop()
            else:
                return False
        return len(stack) == 0
        
class MinStack:

    def __init__(self):
        self.__stack = []

    def push(self, val: int) -> None:
        self.__stack.append(val)

    def pop(self) -> None:
        del self.__stack[-1]

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return min(self.__stack)

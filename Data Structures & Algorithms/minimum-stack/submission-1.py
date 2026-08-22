class MinStack:

    def __init__(self):
        self.__stack = []
        self.__minstack = []

    def push(self, val: int) -> None:
        self.__stack.append(val)
        if self.__minstack:
            val = min(val, self.__minstack[-1])
        self.__minstack.append(val)

    def pop(self) -> None:
        self.__stack.pop()
        self.__minstack.pop()

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__minstack[-1]

class MinStack:

    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if (len(self.minStack) == 0) or (val <= self.minStack[len(self.minStack) - 1]):
            self.minStack.append(val)
        self.mainStack.append(val)     

    def pop(self) -> None:
        if self.mainStack[len(self.mainStack)-1] == self.minStack[len(self.minStack) - 1]:
            self.minStack = self.minStack[:len(self.minStack)-1]
        self.mainStack = self.mainStack[:len(self.mainStack)-1]

    def top(self) -> int:
        return self.mainStack[len(self.mainStack)-1]

    def getMin(self) -> int:
        return self.minStack[len(self.minStack)-1]




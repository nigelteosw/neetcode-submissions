class FreqStack:

    def __init__(self):
        self.maxCount = 0
        self.stacks = {}
        self.count = {}
        

    def push(self, val: int) -> None:
        value = 1 + self.count.get(val, 0)
        self.count[val] = value
        if value > self.maxCount:
            self.maxCount = value
            self.stacks[value] = []
        self.stacks[value].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxCount].pop()
        self.count[res] -= 1
        if not self.stacks[self.maxCount]:
            self.maxCount -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
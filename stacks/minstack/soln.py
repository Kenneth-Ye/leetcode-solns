class MinStack:
    def __init__(self):
        self.nums = []
        self.mins = []

    def push(self, val: int) -> None:
        if len(self.mins) == 0:
            self.mins.append(val)
        elif val <= self.mins[-1]:
            self.mins.append(val)
        self.nums.append(val)

    def pop(self) -> None:
        if len(self.nums) == 0: return
        if self.nums.pop() == self.mins[-1]: self.mins.pop()
         

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.mins[-1]
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack is non increasing
        stack = []
        results = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if len(stack) != 0:
                while (len(stack) != 0 and stack[-1][1] < temperatures[i]):
                    info = stack.pop()
                    results[info[0]] = i - info[0]
            stack.append([i, temperatures[i]])
        return results

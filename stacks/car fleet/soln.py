class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 0 1 2 3 4 5 6 7 8 9 10
        # 1 2     2     1
        #
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for i in range(len(pair)):
            stack.append((target - pair[i][0]) / pair[i][1])
            if (len(stack) >= 2 and stack[-1] <= stack[-2]):
                stack.pop()
        return len(stack)

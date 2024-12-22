class Solution:
    def isValid(self, s: str) -> bool:
        corresponding = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        stack = []
        for char in s:
            if char in '{[(':
                stack.append(char)
                continue
            if len(stack) == 0:
                return False
            closing = stack.pop()
            print(closing)
            if corresponding[char] != closing:
                return False
        return len(stack) == 0

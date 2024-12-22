class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        for char in s:
            if char.isalnum():
                filtered += char
        filtered = filtered.lower()
        for i in range(len(filtered)):
            if (filtered[i] != filtered[-1 - i]):
                return False
        return True

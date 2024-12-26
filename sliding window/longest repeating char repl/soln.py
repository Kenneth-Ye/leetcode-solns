class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        seen = {}
        seen[s[r]] = 1
        max_freq = 1
        max_seen = 1
        while (r < len(s) - 1):
            r += 1
            if s[r] in seen:
                seen[s[r]] += 1
            else:
                seen[s[r]] = 1
            max_freq = max(max_freq, seen[s[r]])
            while (r - l + 1 - max_freq > k):
                seen[s[l]] -= 1
                l += 1
            max_seen = max(max_seen, r - l + 1)
        return max_seen
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # f g h g
        l, r = 0, 0
        seen = set()
        maxSeen = 0
        while (r <= len(s) - 1):
            if (s[r] not in seen):
                print(s[l:r+1], r - l + 1)
                seen.add(s[r])
                maxSeen = max(maxSeen, r - l + 1)
                r += 1
                continue
            else:
                while (s[l] != s[r]):
                    seen.remove(s[l])
                    l += 1
                seen.remove(s[r])
                l += 1
        return maxSeen

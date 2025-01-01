class Solution:
    def minWindow(self, s: str, t: str) -> str:
        perm = {}
        for char in t:
            if char in perm: perm[char] += 1
            else: perm[char] = 1
        
        def is_feasible(chars):
            for key in chars:
                if chars[key] > 0:
                    return False
            return True

        minSub = s
        solnFound = False
        l, r = 0, 0
        while (r < len(s) and l <= r):
            if s[r] in perm: perm[s[r]] -= 1
            while (is_feasible(perm)):
                if len(s[l:r+1]) <= len(minSub):
                    minSub = s[l:r+1]
                    solnFound = True
                if s[l] in perm: perm[s[l]] += 1
                l += 1
            r += 1
        if solnFound: return minSub
        else: return ""

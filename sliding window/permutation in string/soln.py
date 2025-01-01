class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = {}
        for char in s1:
            if char in perm:
                perm[char] += 1
            else:
                perm[char] = 1

        def is_feasible():
            for key in perm:
                if perm[key] != 0:
                    return False
            return True
        
        l, r = 0, 0
        while (r < len(s2)):
            if s2[r] in perm: perm[s2[r]] -= 1
            if (r - l + 1 > len(s1)):
                if s2[l] in perm: perm[s2[l]] += 1
                l += 1
            if is_feasible(): return True
            r += 1
        return False

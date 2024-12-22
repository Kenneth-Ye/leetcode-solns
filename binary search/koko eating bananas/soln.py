class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pileMax = piles[0]
        for i in range(1, len(piles)):
            pileMax = max(pileMax, piles[i])
        # binary search 1 to pileMax
        l = 1
        r = pileMax
        currMin = pileMax
        while(l <= r):
            # check mid
            mid = l + (r - l) // 2
            hours = 0
            for i in range(len(piles)):
                hours += -(piles[i] // -mid)
            if hours <= h:
                currMin = mid
                r = mid - 1
                continue
            else:
                l = mid + 1
        return currMin

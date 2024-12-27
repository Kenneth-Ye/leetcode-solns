class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = deque()
        res = []
        l, r = 0, 0

        while (r < len(nums)):
            while(maxes and nums[maxes[-1]] < nums[r]):
                maxes.pop()
            maxes.append(r)

            if (r - l + 1) == k:
                res.append(nums[maxes[0]])
                l += 1
            r += 1

            if (maxes[0] == l - 1):
                maxes.popleft()
        return res
            
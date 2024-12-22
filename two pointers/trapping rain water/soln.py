class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]

        trapped_water = 0
        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                trapped_water += max(max_left - height[left], 0)
            else:
                right -= 1
                max_right = max(max_right, height[right])
                trapped_water += max(max_right - height[right], 0)

        return trapped_water

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # [1,7,2,5,4,7,3,6]
        # [1], [6]
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            cur_area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, cur_area)

            # if the left incremented bar is greater, 
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_area

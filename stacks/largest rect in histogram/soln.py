class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            if (len(stack) != 0 and heights[i] >= heights[stack[-1]]):
                stack.append(i)
            elif (len(stack) != 0 and heights[i] < heights[stack[-1]]):
                while (len(stack) != 0 and heights[i] < heights[stack[-1]]):
                    index = stack.pop()
                    width = i
                    if (len(stack) != 0): width = i - stack[-1] - 1
                    area = width * heights[index]
                    maxArea = max(area, maxArea)
                stack.append(i)
            else:
                stack.append(i)
        while stack:
            index = stack.pop()
            if stack:
                width = len(heights) - stack[-1] - 1
            else:
                width = len(heights)
            area = heights[index] * width
            maxArea = max(area, maxArea)
        return maxArea
# maxArea = 7    
# stack [1, 3, 4, 5]
 #######
 #
 ####### 
 ##
 ##
 ####

#
###
#######

# right stack []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            if (nums[i] in numbers):
                return [numbers[nums[i]], i]
            else:
                numbers[target - nums[i]] = i

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = -1
        for i in range(len(nums)):
            if nums[abs(nums[i])] < 0:
                duplicate = abs(nums[i])
            else:
                nums[abs(nums[i])] = -1 * nums[abs(nums[i])]
            print(nums, duplicate)

        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        return duplicate

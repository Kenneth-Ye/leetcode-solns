class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [4 5 6 7]
        l, r = 0, len(nums) - 2
        while(l <= r):
            mid = l + (r - l) // 2
            print(l, r, mid)
            if (nums[mid] >= nums[mid + 1]):
                return nums[mid + 1]
            elif (nums[l] > nums[mid]):
                r = mid - 1
            else:
                l = mid + 1
        return nums[0]
    
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # [5 -1 0 1 2 ]
        while (l <= r):
            mid = l + (r - l) // 2
            # left side
            if (nums[mid] == target): return mid
            elif (nums[l] <= nums[mid]):
                # know that rs contains the pivot
                if (target >= nums[l] and target <= nums[mid]):
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # know that ls contains the pivot
                if (target >= nums[mid] and target <= nums[r]):
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
    
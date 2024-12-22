class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_in_arr = {}   
        for i in range(len(nums)):
            nums_in_arr[nums[i]] = True
        
        longest = 0
        for n in nums_in_arr:
            if ( n - 1 not in nums_in_arr):
                length = 1
                while (n + length) in nums_in_arr:
                    length += 1
                longest = max(longest, length)

        return longest

            
        
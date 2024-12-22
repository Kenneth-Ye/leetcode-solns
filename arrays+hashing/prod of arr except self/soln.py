class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
        if prod != 0:
            for i in range(len(nums)):
                arr.append(int(prod / nums[i]))
            return arr
        else:
            for i in range(len(nums)):
                if nums[i] != 0:
                    arr.append(0)
                else:
                    prod_nozero = 1
                    for j in range(len(nums)):
                        if j != i:
                            prod_nozero *= nums[j]
                    if prod_nozero == 0:
                        return [0] * len(nums)
                    else:
                        arr.append(prod_nozero)
            return arr

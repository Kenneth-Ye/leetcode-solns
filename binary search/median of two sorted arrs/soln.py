class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # [1,2] [3]
        # L[1]
        # R[3]
        totalLength = len(nums1) + len(nums2)
        half = totalLength // 2
        A, B = nums1, nums2
        if (len(nums2) < len(nums1)):
            temp = A
            A = B
            B = temp
        l, r = 0, len(A) - 1
        while True:
            mid = l + (r - l) // 2
            other = half - mid - 2

            Aleft = A[mid] if mid >= 0 else float("-infinity")
            Aright = A[mid + 1] if mid + 1 <= len(A) - 1 else float("infinity")
            Bleft = B[other] if other >= 0 else float("-infinity")
            Bright = B[other + 1] if other + 1 <= len(B) - 1 else float("infinity")

            # good partition
            if (Bleft <= Aright and Aleft <= Bright):
                if (totalLength % 2):
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = mid - 1
            else:
                l = mid + 1

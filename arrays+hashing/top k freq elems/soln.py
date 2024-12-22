class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        for num in count:
            freq[count[num]].append(num)
        topk = []
        topk_count = 0
        for i in range(len(freq) - 1, 0, -1):
            for j in range(len(freq[i])):
                topk.append(freq[i][j])
                topk_count += 1
            if topk_count == k:
                return topk
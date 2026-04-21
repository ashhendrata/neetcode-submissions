class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # checking to see if there's a num - 1
        nums_set = set(nums)
        best = 0

        for num in nums:
            if num - 1 not in nums_set:
                length = 1
                while num + length in nums_set:
                    length += 1
                best = max(length, best)

        
        return best
















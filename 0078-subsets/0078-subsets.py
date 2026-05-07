class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(index, current):
            # Add current subset
            result.append(current[:])

            # Generate subsets
            for i in range(index, len(nums)):
                current.append(nums[i])          # choose
                backtrack(i + 1, current)       # explore
                current.pop()                   # un-choose

        backtrack(0, [])
        return result
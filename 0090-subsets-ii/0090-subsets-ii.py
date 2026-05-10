class Solution:
    def subsetsWithDup(self, nums):
        
        nums.sort()   # Sort to handle duplicates
        result = []
        
        def backtrack(start, path):
            
            # Add current subset
            result.append(path[:])
            
            for i in range(start, len(nums)):
                
                # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                # Include current element
                path.append(nums[i])
                
                # Recurse
                backtrack(i + 1, path)
                
                # Backtrack
                path.pop()
        
        backtrack(0, [])
        
        return result
        
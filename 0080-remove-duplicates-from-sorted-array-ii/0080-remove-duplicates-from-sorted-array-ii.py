class Solution:
    def removeDuplicates(self, nums):
        
        # Pointer for placing valid elements
        k = 2
        
        # If array has 2 or fewer elements
        if len(nums) <= 2:
            return len(nums)
        
        # Start from index 2
        for i in range(2, len(nums)):
            
            # Keep element if it is not same as nums[k-2]
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        
        return k        
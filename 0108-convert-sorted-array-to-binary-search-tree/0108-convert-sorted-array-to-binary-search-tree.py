class Solution:
    def sortedArrayToBST(self, nums):
        
        # If there are no elements
        if not nums:
            return None
        
        # Find the middle element
        mid = len(nums) // 2
        
        # Create the root node
        root = TreeNode(nums[mid])
        
        # Create the left subtree
        root.left = self.sortedArrayToBST(nums[:mid])
        
        # Create the right subtree
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return root
    

        
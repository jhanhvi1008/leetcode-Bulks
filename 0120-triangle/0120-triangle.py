class Solution:
    def minimumTotal(self, triangle):
        # Start from the second-last row
        for i in range(len(triangle) - 2, -1, -1):
            
            # Check each element in the current row
            for j in range(len(triangle[i])):
                
                # Choose the smaller of the two possible paths
                triangle[i][j] += min(
                    triangle[i + 1][j],
                    triangle[i + 1][j + 1]
                )
        
        # Top element now contains the minimum path sum
        return triangle[0][0]
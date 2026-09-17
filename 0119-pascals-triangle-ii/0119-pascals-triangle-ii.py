class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        
        for k in range(1, rowIndex + 1):
            # Calculate next element directly using the preceding value
            next_val = row[-1] * (rowIndex - k + 1) // k
            row.append(next_val)
            
        return row
        
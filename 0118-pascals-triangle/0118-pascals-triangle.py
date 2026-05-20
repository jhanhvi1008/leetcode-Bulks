class Solution:
    def generate(self, numRows):
        triangle = []

        for i in range(numRows):
            # Start each row with 1's
            row = [1] * (i + 1)

            # Fill middle values
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle


# Example Usage
sol = Solution()

print(sol.generate(5))
print(sol.generate(1))
        
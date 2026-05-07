class Solution:
    def combine(self, n: int, k: int):
        result = []

        def backtrack(start, path):

            # If combination size becomes k
            if len(path) == k:
                result.append(path[:])
                return

            # Generate combinations
            for num in range(start, n + 1):
                path.append(num)
                backtrack(num + 1, path)
                path.pop()

        backtrack(1, [])
        return result
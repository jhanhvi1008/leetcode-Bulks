class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, path, target):
            if target == 0:
                result.append(path[:])
                return
            
            if target < 0:
                return

            for i in range(start, len(candidates)):
                # choose the number
                path.append(candidates[i])
                
                # stay at i (reuse allowed)
                backtrack(i, path, target - candidates[i])
                
                # backtrack
                path.pop()

        backtrack(0, [], target)
        return result
        
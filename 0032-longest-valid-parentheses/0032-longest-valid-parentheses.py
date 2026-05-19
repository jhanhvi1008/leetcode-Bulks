class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]   # Base index
        max_length = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()

                # If stack becomes empty, push current index
                if not stack:
                    stack.append(i)
                else:
                    # Calculate valid substring length
                    max_length = max(max_length, i - stack[-1])

        return max_length
        